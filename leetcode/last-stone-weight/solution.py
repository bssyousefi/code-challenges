# First solution (beats 100%) (heap)
class Heap:
    def __init__(self, l):
        self.data = l
        self.newHeap()

    def newHeap(self):
        n = len(self.data)
        for i in range((n-1)//2, -1, -1):
            self.heapify(n, i)

    def heapify(self, n, i):
        max_ = i
        l = i*2+1
        r = i*2+2
        if l < n and self.data[l] > self.data[max_]:
            max_ = l

        if r < n and self.data[r] > self.data[max_]:
            max_ = r

        if max_ != i:
            self.data[i], self.data[max_] = self.data[max_], self.data[i]
            self.heapify(n, max_)

    def pop(self):
        ret = self.data[0]
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data.pop()
        self.heapify(len(self.data), 0)
        return ret

    def push(self, val):
        self.data.append(val)
        self.newHeap()

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = Heap(stones)
        while len(h.data) > 1:
            s1 = h.pop()
            s2 = h.pop()
            if s1 > s2:
                h.push(s1-s2)
        if len(h.data):
            return h.data[0]
        else:
            return 0
