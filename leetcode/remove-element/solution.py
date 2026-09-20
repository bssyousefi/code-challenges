# First solution (beats 100%)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        removals = []
        for i in range(n):
            if nums[i] == val:
                removals.append(i)
        offset = 0
        for i in removals:
            nums.pop(i-offset)
            offset += 1

        return n - len(removals)
