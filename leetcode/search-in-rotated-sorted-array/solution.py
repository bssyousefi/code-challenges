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

