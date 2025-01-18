# First solution (beats 5%) (min heap)
class Heap:
    def __init__(self, nums):
        self.data = nums
        self.l = len(self.data)

    def heap(self):
        for i in range((self.l-1)//2,-1,-1):
            self.heapify(i)

    def heapify(self, i):
        min_ = i
        l, r = 2*i+1, 2*i+2

        if l < self.l and self.data[l] < self.data[min_]:
            min_ = l
        if r < self.l and self.data[r] < self.data[min_]:
            min_ = r

        if min_ != i:
            self.data[i], self.data[min_] = self.data[min_], self.data[i]
            self.heapify(min_)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = Heap(nums[:k])
        h.heap()
        for i in range(k, len(nums)):
            if nums[i] > h.data[0]:
                h.data[0] = nums[i]
                h.heapify(0)

        return h.data[0]
# Second solution (beats 87%) (built-in sort)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
