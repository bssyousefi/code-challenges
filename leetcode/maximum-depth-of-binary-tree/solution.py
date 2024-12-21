# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        _max = 0
        if root.left:
            _max = max(_max, self.maxDepth(root.left))
        if root.right:
            _max = max(_max, self.maxDepth(root.right))
        return _max + 1
