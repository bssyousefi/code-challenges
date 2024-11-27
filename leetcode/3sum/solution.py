# First solution (beats 5%)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        i, j = 0, len(nums) - 1
        ret = []
        while i < j:
            k = i + 1
            while k < j:
                if s[i] + s[j] + s[k] == 0:
                    ret.append((s[i], s[j], s[k]))
                    k += 1
                elif s[i] + s[j] + s[k] < 0:
                    k += 1
                else:
                    j -= 1
            i += 1
            j = len(nums) - 1
        return [list(i) for i in set(ret)]

# Second solution (beats 7%)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        i, k, j = 0, 1, len(nums) - 1
        ret = set()
        while i < len(nums)-2:
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if s[i] + s[k] + s[j] == 0:
                    ret.add((s[i], s[k], s[j]))
                    k += 1
                    j -= 1
                elif s[i] + s[k] + s[j] < 0:
                    k += 1
                else:
                    j -= 1
            i += 1

        return [list(i) for i in ret]

# Third solution (beats 24%) (2nd solution optimized)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        i, k, j = 0, 1, len(nums) - 1
        ret = set()
        while i < len(nums)-2:
            if i > 0 and s[i] == s[i-1]:
                i += 1
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
                if s[i] + s[k] + s[j] == 0:
                    ret.add((s[i], s[k], s[j]))
                    k += 1
                    j -= 1
                elif s[i] + s[k] + s[j] < 0:
                    k += 1
                else:
                    j -= 1
            i += 1

        return [list(i) for i in ret]

# Forth solution (beats 87%) (3rd solution optimized)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        i, k, j = 0, 1, len(nums) - 1
        ret = set()
        while i < len(nums)-2:
            if s[i] > 0:
                break
            if i > 0 and s[i] == s[i-1]:
                i += 1
                continue
            k = i + 1
            j = len(nums) - 1
            while k < j:
                v = s[i] + s[k] + s[j]
                if v == 0:
                    ret.add((s[i], s[k], s[j]))
                    k += 1
                    j -= 1
                elif v < 0:
                    k += 1
                else:
                    j -= 1
            i += 1

        return [list(i) for i in ret]
