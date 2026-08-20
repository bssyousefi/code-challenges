# First solution (beats 9%) (DFS)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False]*n for _ in range(m)]
        MOVES = [(0,1),(0,-1),(1,0),(-1,0)]
        _max = 0
        def dfs(i,j):
            visit[i][j] = True
            if grid[i][j] == 0:
                return 0
            ret = 1
            for dy,dx in MOVES:
                if dy+i>=0 and dy+i<m and dx+j>=0 and dx+j<n and not visit[dy+i][dx+j]:
                    ret += dfs(dy+i, dx+j)
            return ret

        for i in range(m):
            for j in range(n):
                ret = dfs(i,j)
                if _max < ret:
                    _max = ret
        return _max

# Second solution (beats 43%) (DFS)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False]*n for _ in range(m)]
        MOVES = [(0,1),(0,-1),(1,0),(-1,0)]
        _max = 0
        def dfs(i,j):
            visit[i][j] = True
            if grid[i][j] == 0:
                return 0
            ret = 1
            for dy,dx in MOVES:
                if dy+i>=0 and dy+i<m and dx+j>=0 and dx+j<n and not visit[dy+i][dx+j]:
                    ret += dfs(dy+i, dx+j)
            return ret

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visit[i][j]:
                    ret = dfs(i,j)
                    if _max < ret:
                        _max = ret
        return _max

