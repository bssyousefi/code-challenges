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

# Second solution (beats 98%) (same solution)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        max_t = nums[0]
        for i in range(1, len(nums)):
            v = nums[i]
            if max_t >= 0:
                max_t += v
            else:
                max_t = v
            if max_t > max_:
                max_ = max_t

        return max_
