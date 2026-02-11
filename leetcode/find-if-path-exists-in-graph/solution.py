# First solution (beats 54%), recursive DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = defaultdict(set)
        for i, j in edges:
            paths[i].add(j)
            paths[j].add(i)

        visited = [False] * n

        def dfs(i: int):
            ret = False
            if i == destination:
                return True
            for j in paths[i]:
                if not visited[j]:
                    visited[j] = True
                    ret = dfs(j)
                    if ret:
                        break
            return ret

        return dfs(source)

# Second solution (beats 89%), iterative DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = [[] for _ in range(n)]
        for i, j in edges:
            paths[i].append(j)
            paths[j].append(i)

        visited = [False] * n

        stack = [source]
        while stack:
            i = stack.pop()
            if i == destination:
                return True
            if visited[i]:
                continue
            visited[i] = True
            for j in paths[i]:
                if not visited[j]:
                    stack.append(j)

        return False
