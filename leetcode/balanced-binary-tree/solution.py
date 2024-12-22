# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, m = self.checkBalance(root)
        return m

    def checkBalance(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root is None:
            return 0, True
        l, lB = self.checkBalance(root.left)
        r, rB = self.checkBalance(root.right)

        return max(l,r)+1, lB and rB and abs(l-r) < 2
