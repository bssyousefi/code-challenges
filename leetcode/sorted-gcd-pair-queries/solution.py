# First solution (Memory limit)
class Solution:
    def __init__(self):
        self.cache = {}
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * (n * (n-1) // 2)
        counter = 0
        for i in range(n):
            for j in range(i+1, n):
                max_ = max(nums[i], nums[j])
                min_ = min(nums[i], nums[j])
                if (max_, min_) not in self.cache:
                    ll = self.gcd(max_, min_)
                    self.cache[(max_, min_)] = ll
                else:
                    ll = self.cache[(max_, min_)]
                l[counter] = ll
                counter += 1


        l = sorted(l)
        return [l[i] for i in queries]

    def gcd(self, i: int, j: int) -> int:
        while j > 0:
            i = i%j
            i, j = j, i
        return i


# Second solution (Beats 34%)
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            exact[d] = c * (c - 1) // 2
            for multiple in range(2 * d, mx + 1, d):
                exact[d] -= exact[multiple]

        prefix = [0] * (mx + 1)
        for d in range(1, mx + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1))

        return ans

# Third solution (Beats 96%) (Pythononic version of the second solution)
class Solution:
    def gcdValues(self, A: list[int], queries: list[int]) -> list[int]:
        mx = max(A)
        freq = [0] * (mx + 1)
        for a in A: 
            freq[a] += 1

        GCD = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])

        GCD = list(accumulate(GCD))

        return [bisect.bisect_right(GCD, q) for q in queries]
