# First solution (beats 10%)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        tmp = [*nums[:k]]
        for i in range(k):
            nums[i] = nums[l - k + i]

        for i in range(k, l):
            tmp.append(nums[i])
            nums[i] = tmp.pop(0)

# Second solution (beats 74%)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        tmp = [*nums[:l-k]]
        for i in range(k):
            nums[i] = nums[l - k + i]

        for i in range(k, l):
            nums[i] = tmp[i-k]
