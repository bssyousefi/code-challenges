# First solution (beats 15%) (Prim's algorithm)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = defaultdict(list)
        l = len(points)
        for i in range(l):
            for j in range(i+1, l):
                heapq.heappush(costs[i], (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), j))
                heapq.heappush(costs[j], (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i))

        seen = {0}
        ret = 0
        while len(seen) < l:
            _min = None
            for i in seen:
                while costs[i][0][1] in seen:
                    heapq.heappop(costs[i])
                if _min is None or costs[i][0][0] < costs[_min][0][0]:
                    _min = i

            cost, next = heapq.heappop(costs[_min])
            ret += cost
            seen.add(next)

        return ret
# Second solution (beats 9%) (Prim's algorithm, double heap)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = defaultdict(list)
        l = len(points)
        for i in range(l):
            for j in range(i+1, l):
                heapq.heappush(costs[i], (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), j))
                heapq.heappush(costs[j], (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i))

        seen = {0}
        seenHeap = costs[0][:]
        ret = 0
        while seenHeap:
            cost, next = heapq.heappop(seenHeap)
            if next not in seen:
                seen.add(next)
                ret += cost
                for i in costs[next]:
                    if i[1] not in seen:
                        heapq.heappush(seenHeap, i)

        return ret
# Third solution (beats 88%) (Kruskal's algorithm)
class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])

        return self.parents[i]

    def union(self, i, j):
        iRep = self.find(i)
        jRep = self.find(j)
        self.parents[jRep] = iRep


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        l = len(points)
        for i in range(l):
            for j in range(i+1, l):
                heapq.heappush(costs, (abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i, j))

        seen = DisjointSet(l)
        counter = 0
        ret = 0

        while costs:
            cost, point1, point2 = heapq.heappop(costs)
            p1 = seen.find(point1)
            p2 = seen.find(point2)
            if p1 != p2:
                counter += 1
                seen.union(p1, p2)
                ret += cost
            if counter == l-1:
                break

        return ret
# Fourth solution (beats 99%) (Prim's algorithm)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = [float("inf") for _ in points]
        ret = 0
        l = len(points)

        for i in range(l-1):
            for j in range(i+1, l):
                if (m:= abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])) < costs[j]:
                    costs[j] = m
                if costs[j] < costs[i+1]:
                    costs[j], costs[i+1] = costs[i+1], costs[j]
                    points[j], points[i+1] = points[i+1], points[j]
            ret += costs[i+1]

        return ret
