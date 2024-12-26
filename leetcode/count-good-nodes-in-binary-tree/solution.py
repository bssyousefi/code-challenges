# First solution (beats 64%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.getCountOfGoodNodes(root, root.val)

    def getCountOfGoodNodes(self, root: TreeNode, max_: int) -> int:
        if root is None:
            return 0
        if root.val >= max_:
            ret = 1
            max_ = root.val
        else:
            ret = 0

        ret += self.getCountOfGoodNodes(root.left, max_)
        ret += self.getCountOfGoodNodes(root.right, max_)
        return ret
