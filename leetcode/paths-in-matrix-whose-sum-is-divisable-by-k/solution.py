# First Solution (Timeout exceeded) (BFS)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        queue = [(0,0,grid[0][0])]
        m = len(grid)
        n = len(grid[0])
        counter = 0
        while queue:
            i,j,v = queue.pop(0)
            if i == m-1 and j == n-1:
                if v%k == 0:
                    counter += 1
            if i < m-1:
                queue.append((i+1, j, v+grid[i+1][j]))
            if j < n-1:
                queue.append((i, j+1, v+grid[i][j+1]))

        return counter


# Second Solution (beats 42%) (DP)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        rec = [[defaultdict(int) for _ in range(n)] for _ in range(m)]
        rec[0][0][grid[0][0]%k] += 1
        for i in range(m):
            for j in range(n):
                v = grid[i][j]%k
                if i > 0:
                    for l in rec[i-1][j]:
                        if (vv := rec[i-1][j][l]) > 0:
                            rec[i][j][(l+v)%k] += vv
                if j > 0:
                    for l in rec[i][j-1]:
                        if (vv := rec[i][j-1][l]) > 0:
                            rec[i][j][(l+v)%k] += vv

        return rec[-1][-1][0]%(10**9+7)


#Third Solution (beats 14%) (DP + BFS)
# Basically same as the second solution from different angle using BFS
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        l = defaultdict(lambda: defaultdict(int))
        rmax, cmax = len(grid), len(grid[0])
        BIG_MODULO = int(1e9 + 7)
        seen = set()
        q = deque()
        q.append((0,0))
        l[(0,0)][0] = 1
        while q:
            i, j = q.popleft()
            if (i,j) in seen:
                continue
            seen.add((i,j))
            if i >= rmax or j >= cmax:
                continue
            s = grid[i][j]
            for n, m in l[(i,j)].items():
                v = (s + n) % k
                l[(i, j+1)][v] += m
                l[(i, j+1)][v] %= BIG_MODULO
                l[(i+1, j)][v] += m
                l[(i+1, j)][v] %= BIG_MODULO
            q.extend([(i, j+1), (i+1, j)])

        return l[(rmax,cmax-1)][0]
