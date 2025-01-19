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
