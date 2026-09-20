# First solution (beats 62%) (BFS + min heap queue)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        queue = [(0,0,0)]
        visit = [[None]*n for _ in range(m)]
        while queue:
            effort, i, j = heapq.heappop(queue)
            if i == m-1 and j == n-1:
                return effort

            for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
                if dy+i >= 0 and dy+i < m and dx+j >= 0 and dx+j < n:
                    val = max(effort, abs(heights[dy+i][dx+j]-heights[i][j]))
                    if visit[dy+i][dx+j] is None or val < visit[dy+i][dx+j]:
                        visit[dy+i][dx+j] = val
                        heapq.heappush(queue, (val, dy+i, dx+j))

        return 0

