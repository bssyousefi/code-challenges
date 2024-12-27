# First solution (beats 89%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        a, _ = self.getMaxPathSum(root)
        return a

    def getMaxPathSum(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if root is None:
            return 0, 0

        if root.left is None and root.right is None:
            return root.val, root.val
        m = root.val
        la, ra = 0, 0
        if root.left:
            l, la = self.getMaxPathSum(root.left)
            m = max(m, l)

        if root.right:
            r, ra = self.getMaxPathSum(root.right)
            m = max(m, r)

        m = max(m, max(la, ra, la+ra)+root.val)
        return m, max(la, ra, 0) + root.val

