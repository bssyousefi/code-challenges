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
