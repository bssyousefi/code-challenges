# First solution (beats 19%) (BFS + min heap) (mem beats 100%)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(dict)
        for i,j,l in times:
            m[i][j] = l

        q = [(0,k)]
        heapq.heapify(q)
        seen = set()
        ret = 0
        while q:
            t, node = heapq.heappop(q)
            if node in seen:
                continue
            seen.add(node)
            if t > ret:
                ret = t
            for i in m[node]:
                heapq.heappush(q, (t+m[node][i], i))

        return ret if len(seen) == n else -1
# Second solution (beats 34%) (same solution, map -> array)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(dict)
        for i,j,l in times:
            m[i][j] = l

        q = [(0,k)]
        heapq.heapify(q)
        seen = [False]*n
        ret = 0
        while q:
            t, node = heapq.heappop(q)
            if seen[node-1]:
                continue
            seen[node-1] = True
            if t > ret:
                ret = t
            for i in m[node]:
                heapq.heappush(q, (t+m[node][i], i))

        return ret if all(seen) else -1
# Third solution (beats 92%) (same solution, remove useless entries)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(dict)
        for i,j,l in times:
            m[i][j] = l

        q = [(0,k)]
        heapq.heapify(q)
        seen = [False]*n
        tmp = [float("inf")]*n
        tmp[k-1] = 0
        ret = 0
        while q:
            t, node = heapq.heappop(q)
            if seen[node-1]:
                continue
            seen[node-1] = True
            if t > ret:
                ret = t
            for i in m[node]:
                if tmp[i-1] > t+m[node][i]:
                    tmp[i-1] = t+m[node][i]
                    heapq.heappush(q, (t+m[node][i], i))

        return ret if all(seen) else -1
