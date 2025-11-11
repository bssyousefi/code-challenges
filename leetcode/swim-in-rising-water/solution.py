# First Solution (beats 5%)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rets = set()
        n = len(grid)
        mins = defaultdict(lambda : float("inf"))
        seen = set()
        def dfs(i,j, m):
            new_m = max(m, grid[i][j])
            mins[(i,j)] = min(mins[(i,j)], new_m)
            if i > 0 and mins[(i-1,j)] > new_m: dfs(i-1, j,new_m)
            if i < n-1 and mins[(i+1, j)] > new_m: dfs(i+1, j, new_m)
            if j > 0 and mins[(i, j-1)] > new_m: dfs(i, j-1,new_m)
            if j < n-1 and mins[(i, j+1)] > new_m: dfs(i, j+1, new_m)

        dfs(0,0,0)
        return mins[(n-1,n-1)]

# Second Solution (beats 63%)(min heap)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rets = set()
        n = len(grid)
        mins = []
        heapq.heappush(mins, (grid[0][0], 0, 0))
        seen = set((0,0))
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        while mins:
            m, i, j = heapq.heappop(mins)

            if i == n-1 and j == n-1:
                return m

            new_m = max(m, grid[i][j])
            for di, dj in dirs:
                if 0 <= (i+di) < n and 0 <= (j+dj) < n and (i+di,j+dj) not in seen:
                    seen.add((di+i,dj+j))
                    heapq.heappush(mins, (max(m, grid[di+i][dj+j]), di+i, dj+j))

        return 0

# Third Solution (beats 92%)(min heap with 2D seen array)
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rets = set()
        n = len(grid)
        mins = []
        heapq.heappush(mins, (grid[0][0], 0, 0))
        seen = [[False]*n for _ in range(n)]
        seen[0][0] = True
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        while mins:
            m, i, j = heapq.heappop(mins)

            if i == n-1 and j == n-1:
                return m

            new_m = max(m, grid[i][j])
            for di, dj in dirs:
                if 0 <= (i+di) < n and 0 <= (j+dj) < n and not seen[i+di][j+dj]:
                    seen[di+i][dj+j] = True
                    heapq.heappush(mins, (max(m, grid[di+i][dj+j]), di+i, dj+j))

        return 0

