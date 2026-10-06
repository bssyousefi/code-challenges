# First solution (beats 81%) (Kahn's algorithm)
class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        rows = defaultdict(list)
        rowsInDegree = [0] * k
        cols = defaultdict(list)
        colsInDegree = [0] * k
        for above, below in rowConditions:
            rows[above].append(below)
            rowsInDegree[below-1] += 1

        for left, right in colConditions:
            cols[left].append(right)
            colsInDegree[right-1] += 1

        def bfs(routes, inDegrees):
            queue = []
            for i in range(k):
                if inDegrees[i] == 0:
                    queue.append(i+1)
            ret = {}
            counter = 0
            while queue:
                node = queue.pop(0)
                ret[node] = counter
                counter += 1
                for _next in routes[node]:
                    inDegrees[_next-1] -= 1
                    if inDegrees[_next-1] == 0:
                        queue.append(_next)
            if counter < k:
                return {}
            return ret

        rowsOrdered = bfs(rows, rowsInDegree)
        if not rowsOrdered:
            return []
        colsOrdered = bfs(cols, colsInDegree)
        if not colsOrdered:
            return []
        ret = [[0]*k for _ in range(k)]
        for i in range(1,k+1):
            ret[rowsOrdered[i]][colsOrdered[i]] = i

        return ret

