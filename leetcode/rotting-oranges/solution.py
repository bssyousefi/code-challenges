# First solution (beats 88%) (BFS)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = []
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))

        times = 0
        while fresh > 0 and q:
            r, c, t = q.pop(0)

            for i, j in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] != 1:
                    continue
                grid[i][j] = 2
                fresh -= 1
                q.append((i,j,t+1))
                times = t+1

        return -1 if fresh > 0 else times

# Second solution (beats 88%) (BFS) (deque, nested loop)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.appendleft((i,j))

        times = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.pop()
                
                for i, j in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                    if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] != 1:
                        continue
                    grid[i][j] = 2
                    fresh -= 1
                    q.appendleft((i,j))
            times += 1

        return -1 if fresh > 0 else times

# Third solution (beats 86%) (BFS)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = [[False] * n for _ in range(m)]
        fresh_count = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        ret = 0

        for i in range(m):
            for j in range(n):
                match grid[i][j]:
                    case 0:
                        visit[i][j] = True
                    case 2:
                        visit[i][j] = True
                        queue.append((i,j,0))
                    case 1:
                        fresh_count += 1

        while queue:
            i, j, ret = queue.pop(0)
            for di, dj in directions:
                ii = di + i
                jj = dj + j
                if ii >= 0 and ii < m and jj >= 0 and jj < n and not visit[ii][jj]:
                    visit[ii][jj] = True
                    fresh_count -= 1
                    queue.append((ii, jj, ret + 1))

        if fresh_count == 0:
            return ret
        else:
            return -1
