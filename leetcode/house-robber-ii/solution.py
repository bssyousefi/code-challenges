# First solution (beats 100%) (DP)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def cal(i, s=False):
            if i >= n:
                return 0
            elif i == 0:
                return max(cal(2, True)+nums[0], cal(1, False))
            elif i == n-1:
                return 0 if s else nums[i]
            else:
                if (i, s) not in cache:
                    cache[(i, s)] = max(cal(i+2, s)+nums[i], cal(i+1, s))
                return cache[(i, s)]

        return cal(0)
