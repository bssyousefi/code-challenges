# First solution (Timed out)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        data = [[False]*numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            data[a][b] = True

        for _ in range(numCourses-1):
            for i in range(numCourses):
                for j in range(numCourses):
                    if data[i][j]:
                        for k in range(numCourses):
                            if data[j][k] and not data[i][k]:
                                data[i][k] = True

        return [data[i][j] for i,j in queries]

# Second solution (beats 56%) (DFS + memoization)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        cache = {}
        _map = defaultdict(list)
        for a,b in prerequisites:
            _map[b].append(a)

        def dfs(i):
            if i in cache:
                return cache[i]
            cache[i] = set(_map[i])
            for j in _map[i]:
                cache[i].update(dfs(j))

            return cache[i]

        ret = []
        for query in queries:
            dfs(query[1])
            ret.append(query[0] in cache[query[1]])

        return ret

