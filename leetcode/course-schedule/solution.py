# First solution (beats 92%) (DFS)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i,j in prerequisites:
            d[i].append(j)

        visit = set()
        tmp = set()
        def dfs(i):
            if i in tmp:
                return False
            tmp.add(i)
            for j in d[i]:
                if j not in visit:
                    if not dfs(j):
                        return False

            visit.add(i)
            return True
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return False

        return True

# Second solution (beats 87%) (DFS)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = [0] * numCourses
        paths = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            paths[j].append(i)

        def dfs(i):
            for j in paths[i]:
                if visit[j] == 0:
                    visit[j] = 1
                    if not dfs(j):
                        return False
                    visit[j] = 2
                elif visit[j] == 1:
                    return False
            return True

        for i in range(numCourses):
            if visit[i] == 0:
                visit[i] = 1
                if not dfs(i):
                    return False
                visit[i] = 2

        return True

