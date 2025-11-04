# First solution (beats 100%)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        expected = l * (l+1) // 2
        return expected - sum(nums)
