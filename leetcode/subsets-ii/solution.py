# First solution (beats 100%)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.cal(nums)

    def cal(self, nums):
        res = [[]]
        if len(nums) == 0:
            return res
        res.append([nums[0]])
        i = 0
        while i+1 < len(nums) and nums[i+1] == nums[i]:
            res.append([nums[i]] + res[-1])
            i += 1

        v = self.cal(nums[i+1:])
        return [j + k for k in res for j in v]
