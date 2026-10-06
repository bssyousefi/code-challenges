# First solution (beats 100%) (same as search in rotated array without duplicates)
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[m] == nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[m] < nums[l]:
                if target > nums[m]:
                    if target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    r = m - 1
            else:
                if target < nums[m]:
                    if target >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    l = m + 1
        return False
