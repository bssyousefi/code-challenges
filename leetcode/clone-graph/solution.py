# First solution (beats 84%) (DFS)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        def dfs(n):
            m = Node(val=n.val)
            d[n] = m
            for i in n.neighbors:
                if i is not None and i not in d:
                    dfs(i)
                d[n].neighbors.append(d[i])

        if node is None:
            return None

        dfs(node)
        return d[node]

# Second solution (beats 99%) (BFS)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        mapping = {}
        q = [node]
        while q:
            n = q.pop(0)
            if id(n) in mapping:
                continue
            mapping[id(n)] = (n, Node(n.val))
            q.extend([i for i in n.neighbors])
        for i in mapping:
            old, new = mapping[i]
            new.neighbors = [mapping[id(j)][1] for j in old.neighbors]

        return mapping[id(node)][1]

