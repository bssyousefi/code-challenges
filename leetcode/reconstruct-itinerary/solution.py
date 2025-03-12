# First solution (beats 6%) (DFS)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        l = len(tickets)
        c = defaultdict(int)
        for f, t in tickets:
            c[(f,t)] += 1
        m = defaultdict(list)
        for n in c:
            m[n[0]].append((n[1], c[n]))

        for n in m:
            m[n].sort()

        l = len(tickets)
        seen = defaultdict(int)
        def dfs(i, counter):
            counter += 1
            if counter == l+1:
                return [[i]]
            ret = []
            for n in m[i]:
                j = n[0]
                if seen[(i, j)] < n[1]:
                    seen[(i,j)] += 1
                    if res := dfs(j, counter):
                        ret = [[i]+k for k in res]
                        return ret
                    seen[(i,j)] -= 1
            return ret

        ret = dfs("JFK", 0)

        ret.sort()

        return ret[0] if ret else ret
# Second solution (beats 5%) (same solution optimized)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        l = len(tickets)
        c = defaultdict(int)
        m = defaultdict(list)
        for f, t in tickets:
            if c[(f,t)] == 0:
                heapq.heappush(m[f], t)
            c[(f,t)] += 1

        for n in m:
            m[n] = heapq.nsmallest(len(m[n]), m[n])

        l = len(tickets)
        seen = defaultdict(int)
        def dfs(i, counter):
            counter += 1
            if counter == l+1:
                return [i]
            ret = []
            for j in m[i]:
                if seen[(i, j)] < c[(i,j)]:
                    seen[(i,j)] += 1
                    if res := dfs(j, counter):
                        ret = [i]+res
                        return ret
                    seen[(i,j)] -= 1
            return ret

        ret = dfs("JFK", 0)

        return ret

# Third solution (beats 86%) (DFS)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for s,d in tickets[::-1]:
            adj[s].append(d)
        res = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)
        dfs('JFK')
        return res[::-1]
