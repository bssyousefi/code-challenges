# First solution (beats 94%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, m = self.diameterOfBinaryTreeCalc(root)
        return m

    def diameterOfBinaryTreeCalc(self, root: Optional[TreeNode]) -> [int, int]:
        if root is None:
            return 0, 0
        if (root.left is None and root.right is None):
            return 1, 0
        r, l, r_max, l_max = 0, 0, 0, 0
        if root.left:
            l, l_max = self.diameterOfBinaryTreeCalc(root.left)
        if root.right:
            r, r_max = self.diameterOfBinaryTreeCalc(root.right)

        return max(l,r)+1, max(l_max, r_max, l+r)
