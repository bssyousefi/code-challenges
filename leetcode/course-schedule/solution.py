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

# Third solution (beats 89%) (BFS) (Kahn's algorithm)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        routes = defaultdict(list)
        in_degrees = [0]*numCourses

        for a, b in prerequisites:
            routes[b].append(a)
            in_degrees[a] += 1

        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        courses = []
        while queue:
            course = queue.pop(0)
            courses.append(course)
            for c in routes[course]:
                in_degrees[c] -= 1
                if in_degrees[c] == 0:
                    queue.append(c)

        return True if len(courses) == numCourses else False
