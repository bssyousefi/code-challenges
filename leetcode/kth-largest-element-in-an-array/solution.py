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

# Third solution (beats 63%) (max heap)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)
        ret = None
        for _ in range(k):
            ret = heapq.heappop_max(nums)

        return ret

# Fourth solution (beats 26%) (min heap)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        vals = [-i for i in nums]
        heapq.heapify(vals)
        ret = None
        for _ in range(k):
            ret = heapq.heappop(vals)

        return -ret

# Fifth solution (beats 98%) (limited min heap)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        vals = nums[:k]
        heapq.heapify(vals)

        for num in nums[k:]:
            if num > vals[0]:
                heapq.heappushpop(vals, num)

        return vals[0]
