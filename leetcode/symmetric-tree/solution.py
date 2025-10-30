# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if left is None:
            if right is None:
                return True
            return False
        else:
            if right is None:
                return False
        if left.val != right.val:
            return False
        state = self._isSymmetric(left.left, right.right)
        if not state:
            return False
        return self._isSymmetric(left.right, right.left)

