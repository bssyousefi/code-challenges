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
        for i in d:
            if not visit[i-1]:
                if dfs(i) == 0:
                    break

        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in loop and edges[i][1] in loop:
                return edges[i]
        return []
