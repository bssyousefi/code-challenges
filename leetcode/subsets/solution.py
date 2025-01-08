# First solution (beats 100%)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        ret = self.subsets(nums[1:])
        ret = ret + [[*i, nums[0]] for i in ret]
        return ret
