# First solution (beats 7%) (min heap)
class Heap:
    def __init__(self, l):
        self.data = [(i,j, (i**2+j**2)) for i,j in l]
        self.n = len(self.data)
        self.newHeap()

    def newHeap(self):
        for i in range((self.n-1)//2,-1,-1):
            self.heapify(i)

    def heapify(self, i):
        min_ = i
        l, r = 2*i+1, 2*i+2

        if l < self.n and self.data[l][2] < self.data[min_][2]:
            min_ = l

        if r < self.n and self.data[r][2] < self.data[min_][2]:
            min_ = r

        if min_ != i:
            self.data[i], self.data[min_] = self.data[min_], self.data[i]
            self.heapify(min_)

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        i,j,_ = self.data.pop()
        self.n -= 1
        self.heapify(0)
        return [i,j]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = Heap(points)
        ret = [None]*k
        for i in range(k):
            ret[i] = h.pop()

        return ret
# Second solution (beats 10%) (max heap)
class Heap:
    def __init__(self, l):
        self.data = [([i,j], (i**2+j**2)) for i,j in l]
        self.n = len(self.data)
        self.newHeap()

    def newHeap(self):
        for i in range((self.n-1)//2,-1,-1):
            self.heapify(i)

    def heapify(self, i):
        max_ = i
        l, r = 2*i+1, 2*i+2

        if l < self.n and self.data[l][1] > self.data[max_][1]:
            max_ = l

        if r < self.n and self.data[r][1] > self.data[max_][1]:
            max_ = r

        if max_ != i:
            self.data[i], self.data[max_] = self.data[max_], self.data[i]
            self.heapify(max_)

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        i,_ = self.data.pop()
        self.n -= 1
        self.heapify(0)
        return i

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = Heap(points[:k])
        for i in range(k,len(points)):
            if h.data[0][1] > (points[i][0]**2+points[i][1]**2):
                h.data[0] = (points[i], points[i][0]**2+points[i][1]**2)
                h.heapify(0)
        ret = [None] * k
        for i in range(k):
            ret[i] = h.data[i][0]

        return ret
# Third solution (beats 24%) (built-in heap)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)
        vs = [i**2+j**2 for i,j in points]
        for i in points:
            v = i[0]**2+i[1]**2
            d[v].append(i)

        h = heapq.nsmallest(k, vs)
        ret = [None]*k
        for i in range(k):
            ret[i] = d[h[i]].pop()
        return ret
# Forth solution (beats 99%) (built-in sort)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2+x[1]**2)
        return points[:k]
