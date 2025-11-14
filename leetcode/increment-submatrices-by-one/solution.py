# First solution (Timeout)
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ret = [[0]* n for _ in range(n)]
        for query in queries:
            for i in range(query[0], query[2]+1):
                for j in range(query[1], query[3]+1):
                    ret[i][j] += 1
        return ret

# Second solution (beats 82%)
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ret = [[0]* n for _ in range(n)]
        counter = 0
        for query in queries:
            ret[query[0]][query[1]] += 1
            if query[2] < n-1:
                ret[query[2]+1][query[1]] -= 1
            if (query[2] < n-1) and query[3] < n-1:
                ret[query[2]+1][query[3]+1] += 1
            if query[3] < n-1:
                ret[query[0]][query[3]+1] -= 1

        for i in range(n):
            for j in range(1, n):
                ret[i][j] += ret[i][j-1]

        for i in range(1, n):
            for j in range(n):
                ret[i][j] += ret[i-1][j]

        return ret
