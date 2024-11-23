# First solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lr, rl = [1] * l, [1] * l
        for i in range(1,l):
            lr[i] = lr[i-1] * nums[i-1]
            rl[l-1-i] = rl[l-i] * nums[l-i]
        return [lr[i]*rl[i] for i in range(l)]

# Second solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lr = [1] * l
        holder = 1
        for i in range(1,l):
            lr[i] = lr[i-1] * nums[i-1]
        for i in range(1,l):
            holder *= nums[l-i]
            lr[l-1-i] = lr[l-1-i] * holder
        return lr
