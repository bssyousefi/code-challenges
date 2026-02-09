# First solution (beats 5%)
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = []
        m = len(isWater)
        n = len(isWater[0])
        visited = [[False] * n for _ in isWater]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    isWater[i][j] = 0
                    visited[i][j] = True

        neighbors = {(0,1), (0,-1), (1,0), (-1,0)}
        while queue:
            i, j = queue.pop(0)
            for di, dj in neighbors:
                ii = i + di
                jj = j + dj
                if ii >= 0 and ii < m and jj >=0 and jj < n and not visited[ii][jj]:
                    isWater[ii][jj] = isWater[i][j] + 1
                    visited[ii][jj] = True
                    queue.append((ii, jj))

        return isWater
