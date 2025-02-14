# First solution (beats 89%) (greedy)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[-1]
        cur = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if cur >= 0:
                cur += nums[i]
            else:
                cur = nums[i]

            if cur > max_:
                max_ = cur

        return max_
