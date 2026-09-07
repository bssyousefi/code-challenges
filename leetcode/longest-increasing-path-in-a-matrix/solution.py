# First solution (beats 67%) (DFS + memoization)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cache = [[None]*n for _ in range(m)]
        ret = 0
        counter = 0

        def dfs(i,j):
            nonlocal ret
            if cache[i][j] is not None:
                return cache[i][j]
            _max = 1
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                if i+dy < 0 or i+dy >= m or j+dx < 0 or j+dx >= n or matrix[i+dy][j+dx] <= matrix[i][j]:
                    continue
                _max = max(_max, dfs(i+dy,j+dx)+1)
            ret = max(ret, _max)
            cache[i][j] = _max
            return _max

        for i in range(m):
            for j in range(n):
                dfs(i,j)
                if counter == n*m:
                    return ret
        return ret
