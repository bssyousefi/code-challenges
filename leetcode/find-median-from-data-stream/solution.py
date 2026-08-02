# First solution (beats 93%) (min and max heaps)
class MedianFinder:

    def __init__(self):
        self.up = []
        self.down = []
        self.tmp = None

    def addNum(self, num: int) -> None:
        if self.tmp is None:
            if len(self.up) == 0:
                self.tmp = num
            elif self.up[0] < num:
                self.tmp = heapq.heappushpop(self.up, num)
            else:
                self.tmp = -heapq.heappushpop(self.down, -num)
        else:
            if self.tmp < num:
                heapq.heappush(self.up, num)
                heapq.heappush(self.down, -self.tmp)
                self.tmp = None
            else:
                heapq.heappush(self.down, -num)
                heapq.heappush(self.up, self.tmp)
                self.tmp = None

    def findMedian(self) -> float:
        if self.tmp is None:
            return (self.up[0] - self.down[0]) / 2
        else:
            return self.tmp

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Second solution (beats 97%) (min and max heaps)
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def addNum(self, val: int) -> None:
        if len(self.min_heap) == 0 or val > self.min_heap[0]:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappush(self.max_heap, -val)
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))


    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
