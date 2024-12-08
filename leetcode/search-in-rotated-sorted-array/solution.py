class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[l] < nums[m]:
                if nums[m] == target:
                    return m
                elif (nums[m] > target and nums[l] > target) or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] > nums[m]:
                if nums[m] == target:
                    return m
                elif (nums[m] < target and nums[r] < target) or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] == target:
                    return l
                else:
                    l = m + 1

        return -1
# New solution (beats 100%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] < nums[j]:
                    j = m - 1
                elif nums[i] <= target:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if nums[m] > nums[j]:
                    i = m + 1
                elif nums[j] >= target:
                    i = m + 1
                else:
                    j = m - 1
        return i if nums[i] == target else -1
        
