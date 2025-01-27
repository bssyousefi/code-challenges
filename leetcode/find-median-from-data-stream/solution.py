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
