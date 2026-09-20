# First solution (beats 5%)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ret = set()
        i = 0
        while i < n-3:
            j = i+1
            while j < n-2:
                k = j+1
                while k < n-1:
                    l = k+1
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            ret.add(quad)
                            break
                    while k < n-2 and nums[k] == nums[k+1]:
                        k+= 1
                    k += 1
                while j < n-3 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i < n-4 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return [list(quad) for quad in ret]
