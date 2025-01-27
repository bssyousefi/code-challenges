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
