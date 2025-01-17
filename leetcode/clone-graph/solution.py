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
