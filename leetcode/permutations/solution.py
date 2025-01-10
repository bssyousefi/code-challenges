# First solution (beats 100%)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        i = 0
        ret = []
        if len(nums) == 0:
            return [[]]
        while i < len(nums):
            for j in self.permute(nums[:i]+nums[i+1:]):
                ret.append([nums[i]] + j)
            i += 1

        return ret
