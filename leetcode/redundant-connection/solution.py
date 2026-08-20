# First solution (beats 100%) (DFS)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)

        visit = [False] * len(d)
        loop = set()
        def dfs(i, k=-1):
            visit[i-1] = True
            for j in d[i]:
                if j != k:
                    if visit[j-1]:
                        loop.add(j)
                        return j
                    v = dfs(j,i)
                    if v == 0:
                        return 0
                    if v > 0:
                        loop.add(j)
                        if i == v:
                            return 0
                        else:
                            return v
            return -1
        dfs(edges[0][0])

        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in loop and edges[i][1] in loop:
                return edges[i]
        return []

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        routes = defaultdict(list)
        for i,j in edges:
            routes[i].append(j)
            routes[j].append(i)

        visit = set()
        ret = set()
        print(routes)
        def dfs(prev, i):
            nonlocal ret
            if i in visit:
                ret.add(i)
                return False
            visit.add(i)
            for j in routes[i]:
                if j != prev:
                    if not dfs(i, j):
                        if i in ret:
                            return True
                        ret.add(i)
                        return False
            return True

        dfs(None, 1)
        print(ret)
        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in ret and edges[i][1] in ret:
                return edges[i]
