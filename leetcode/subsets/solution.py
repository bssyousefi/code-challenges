# First solution (beats 100%)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        ret = self.subsets(nums[1:])
        ret = ret + [[*i, nums[0]] for i in ret]
        return ret

# Second solution (beats 100%)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        n = len(nums)
        for i in range(n):
            temp = [[nums[i]]]
            for j in range(i+1, n):
                temp.extend([[*t, nums[j]] for t in temp])
            ret.extend(temp)
        return ret
