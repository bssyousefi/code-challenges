# First solution (beats 31%)
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def _con(t,b,l,r):
            n = r-l+1
            if n == 1:
                v = True if grid[t][r] == 1 else False
                return Node(v, True, None, None, None, None)
            offset = n // 2 - 1
            topLeft = _con(t, t+offset,l,l+offset)
            topRight = _con(t,t+offset,l+offset+1,r)
            bottomLeft = _con(t+offset+1,b,l,l+offset)
            bottomRight = _con(t+offset+1,b,l+offset+1,r)
            children = [topLeft, topRight, bottomLeft, bottomRight]
            # print(l,r,t,b,[child.val for child in children])
            if all([i.isLeaf for i in children]):
                s = set()
                for child in children:
                    s.add(child.val)
                if len(s) == 1:
                    return Node(s.pop(), True, None, None, None, None)
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        n = len(grid)
        return _con(0,n-1,0,n-1)
