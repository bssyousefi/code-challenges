# First solution (beats 100%) (DFS)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = [False] * numCourses
        tmp = [False] * numCourses
        ret = []
        d = defaultdict(list)

        for i,j in prerequisites:
            d[i].append(j)

        def dfs(i):
            if visit[i]:
                return True
            if tmp[i]:
                return False
            tmp[i] = True
            for j in d[i]:
                if not dfs(j):
                    return False

            ret.append(i)
            visit[i] = True
            return True

        for i in range(numCourses):
            if not visit[i]:
                if not dfs(i):
                    return []

        return ret
# Second solution (beats 100%) (DFS) (Optimized)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = [0] * numCourses
        ret = []
        d = defaultdict(list)

        for i,j in prerequisites:
            d[i].append(j)

        def dfs(i):
            if visit[i] == 2:
                return True
            if visit[i] == 1:
                return False
            visit[i] = 1
            for j in d[i]:
                if not dfs(j):
                    return False

            ret.append(i)
            visit[i] = 2
            return True

        for i in range(numCourses):
            if visit[i] != 2:
                if not dfs(i):
                    return []

        return ret
