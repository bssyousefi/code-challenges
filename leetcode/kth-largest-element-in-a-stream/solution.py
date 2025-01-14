# First solution (beats 5%)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.ret = []
        self.k = k
        self.initiate(sorted(nums))


    def initiate(self, nums):
        for i in range(self.k):
            if len(nums) > 0:
                self.ret.append(nums.pop())


    def add(self, val: int) -> int:
        if len(self.ret) == 0 or val <= self.ret[-1]:
            if len(self.ret) < self.k:
                self.ret.append(val)
            return self.ret[-1]
        else:
            i = len(self.ret)-1
            while i >= 0 and self.ret[i]<val:
                i -= 1

            self.ret.insert(i+1, val)
            if len(self.ret) > self.k:
                self.ret.pop(-1)
            return self.ret[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Seconds solution (beats 96%) (using heap)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.ret = []
        self.k = k
        self.data = sorted(nums, reverse=True)[:k]
        self.initiate(self.data)

    def initiate(self, nums):
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        if len(self.data) == self.k:
            if self.data[0] <= val:
                heapq.heappushpop(self.data, val)
            return self.data[0]
        else:
            heapq.heappush(self.data, val)
            return self.data[0]
