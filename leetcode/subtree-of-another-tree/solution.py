# First solution (beats 82%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            if subRoot is None:
                return True
            else:
                return False

        c = self.isSameTree(root, subRoot)
        if c:
            return c
        l = self.isSubtree(root.left, subRoot)
        if l:
            return l
        r = self.isSubtree(root.right, subRoot)
        return r

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            return r and l
        elif p is None and q is None:
            return True
        else:
            return False

# Second solution (beats 89%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return False
            if isSame(node, subRoot):
                return True
            return dfs(node.right) or dfs(node.left)

        def isSame(node_a, node_b):
            if node_a is None and node_b is None:
                return True
            elif node_a is None or node_b is None:
                return False
            elif node_a.val != node_b.val:
                return False
            else:
                return isSame(node_a.left, node_b.left) and isSame(node_a.right, node_b.right)

        return dfs(root)
