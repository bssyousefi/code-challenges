# First solution (beats 10%) (new DS)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        minHeap = []
        ret = [-1]*len(queries)
        passed = [False]*len(intervals)
        for i, (s, e) in enumerate(intervals):
            events.append((s, 0, e-s+1, i))
            events.append((e, 2, e-s+1, i))
        for i, j in enumerate(queries):
            events.append((j, 1, i))

        events.sort()
        for event in events:
            if event[1] == 0:
                heapq.heappush(minHeap, (event[2], event[3]))
            elif event[1] == 2:
                passed[event[3]] = True
            else:
                while minHeap and passed[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    ret[event[2]] = minHeap[0][0]

        return ret
# Second solution (beats 75%) (minHeap)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        l = len(intervals)
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < l and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(minHeap, (e-s+1, e))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1
        return [res[q] for q in queries]
