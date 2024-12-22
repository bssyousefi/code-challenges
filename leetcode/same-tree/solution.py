# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
