# beats (100%)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            m = (l+r)//2
            if nums[l] < nums[r]:
                return nums[l]
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[r]
# beats (100%)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i+j) // 2
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
        return nums[i]
