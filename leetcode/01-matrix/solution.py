# First solution (beats 21%)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        m = len(mat)
        n = len(mat[0])
        visit = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    visit[i][j] = True
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if ii >= 0 and ii < m and jj >= 0 and jj < n and not visit[ii][jj]:
                    visit[ii][jj] = True
                    mat[ii][jj] = mat[i][j] + 1
                    queue.append((ii, jj))

        return mat
