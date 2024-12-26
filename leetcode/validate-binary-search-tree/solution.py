# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBst(root)

    def isValidBst(self, root: Optional[TreeNode], min_: int = None, max_: int = None):
        if root is None:
            return True
        ret = True
        if min_ is not None and root.val <= min_:
            return False
        if max_ is not None and root.val >= max_:
            return False
        ret = ret and self.isValidBst(root.left, min_=min_, max_=root.val)
        ret = ret and self.isValidBst(root.right,min_=root.val, max_=max_)
        return ret
