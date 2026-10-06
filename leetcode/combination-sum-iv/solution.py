# First solution (beats 100%) (DP top down with memoization)
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        cache = {}
        def cal(i):
            if i in cache:
                return cache[i]
            ret = 0
            for num in nums:
                if num < i:
                    ret += cal(i-num)
                elif num == i:
                    ret += 1
            cache[i] = ret
            return ret

        return cal(target)
