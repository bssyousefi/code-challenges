# First solution (beats 66%) (BFS)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ret += 1
                    self.bfs(grid, i, j)

        return ret

    def bfs(self, grid, i, j):
        q = [(i,j)]
        while q:
            i,j = q.pop(0)
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i < len(grid) - 1:
                    q.append((i+1,j))
                if j < len(grid[i]) - 1:
                    q.append((i,j+1))
                if i > 0:
                    q.append((i-1,j))
                if j > 0:
                    q.append((i,j-1))
# Second solution (beats 88%) (Optimized BFS)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ret += 1
                    self.bfs(grid, i, j)

        return ret

    def bfs(self, grid, i, j):
        q = [(i,j)]
        while q:
            i,j = q.pop(0)
            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i < len(grid) - 1 and grid[i+1][j] == '1':
                    q.append((i+1,j))
                if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
                    q.append((i,j+1))
                if i > 0 and grid[i-1][j] == '1':
                    q.append((i-1,j))
                if j > 0 and grid[i][j-1] == '1':
                    q.append((i,j-1))
# Third solution (beats 91%) (DFS)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ret += 1
                    self.dfs(grid, i, j)

        return ret

    def dfs(self, grid, i, j):
        grid[i][j] = '0'
        if i < len(grid) - 1 and grid[i+1][j] == '1':
            self.dfs(grid, i+1,j)
        if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
            self.dfs(grid, i,j+1)
        if i > 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1,j)
        if j > 0 and grid[i][j-1] == '1':
            self.dfs(grid, i,j-1)

# Forth solution (beats 97%) (Optimized DFS)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        def dfs(i, j):
            grid[i][j] = '0'
            if i < len(grid) - 1 and grid[i+1][j] == '1':
                self.dfs(grid, i+1,j)
            if j < len(grid[i]) - 1 and grid[i][j+1] == '1':
                self.dfs(grid, i,j+1)
            if i > 0 and grid[i-1][j] == '1':
                self.dfs(grid, i-1,j)
            if j > 0 and grid[i][j-1] == '1':
                self.dfs(grid, i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ret += 1
                    dfs(i, j)

        return ret
