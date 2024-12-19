# First solution ( beats 95%)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0] * (len(nums) - 1)
        for i in nums:
            if l[i-1] == 0:
                l[i-1] = 1
            else:
                return i

# Another solutiton( beats 53%) (fast-slow solution)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
