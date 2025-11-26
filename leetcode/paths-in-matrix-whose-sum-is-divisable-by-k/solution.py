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
