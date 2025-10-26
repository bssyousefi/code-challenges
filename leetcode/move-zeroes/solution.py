# First solution (beats 17%)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            if nums[l] != 0:
                if r == l:
                    r += 1
                l += 1
                continue
            if nums[r] == 0:
                r += 1
                continue
            nums[l], nums[r] = nums[r], nums[l]

# Second solution (beats 84%)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
