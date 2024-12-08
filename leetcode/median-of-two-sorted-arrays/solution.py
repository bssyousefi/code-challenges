# First solution (beats 100%) (many if clauses)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j, l, r = -1, len(nums1) - 1, -1, len(nums2) - 1
        _len = len(nums1)+len(nums2)
        s = _len // 2 + 1
        while s > 0:
            if s % 2 == 0:
                ss = s // 2
            else:
                ss = s // 2 + 1
            if i == j:
                l += s
                break
            if l == r:
                i += s
                break
            if j-i <= ss:
                m = j
                n = l + (2 if s==ss else s) - (j-i)
            elif r-l <= ss:
                n = r
                m = i + (2 if s==ss else s) - (r-l)
            else:
                m = i + ss
                n = l + ss
            if nums1[m] < nums2[n]:
                s -= m - i
                i = m

            elif nums1[m] > nums2[n]:
                s -= n - l
                l = n

            else:
                s -= m - i + n - l
                l = n
                i = m
                if s == -1:
                    l -= 1
                break

        if _len % 2 == 0:
            if l == -1:
                return (nums1[i] + nums1[i-1]) / 2
            elif i == -1:
                return (nums2[l] + nums2[l-1]) / 2
            if nums1[i] < nums2[l]:
                if l > 0 and nums1[i] < nums2[l-1]:
                    return (nums2[l] + nums2[l-1]) / 2
                else:
                    return (nums2[l] + nums1[i]) / 2
            else:
                if i > 0 and nums1[i-1] > nums2[l]:
                    return (nums1[i] + nums1[i-1]) / 2
                else:
                    return (nums1[i] + nums2[l]) / 2
        else:
            if l == -1:
                return nums1[i]
            elif i == -1:
                return nums2[l]
            return max(nums1[i], nums2[l])

# Other solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            S, B = nums1, nums2
        else:
            S, B = nums2, nums1

        i, j = 0, len(S) - 1
        s = (len(nums1) + len(nums2)) // 2
        while True:
            k = (i + j) // 2
            l = s - 1 - k - 1
            Sl = S[k] if k >= 0 else float("-infinity")
            Sr = S[k+1] if k < len(S) - 1 else float("infinity")
            Bl = B[l] if l >= 0 else float("-infinity")
            Br = B[l+1] if l < len(B) - 1 else float("infinity")
            if Sl<=Br and Bl<=Sr:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(Br, Sr)
                else:
                    return (max(Sl,Bl) + min(Sr,Br)) / 2
            if Sl > Br:
                j = k - 1
            else:
                i = k + 1
