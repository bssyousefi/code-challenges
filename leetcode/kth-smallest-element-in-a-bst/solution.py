# First solution (beats 6%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ret = self.getKthSmallest(root)
        return ret[k-1]

    def getKthSmallest(self, root: Optional[TreeNode]):
        if root is None:
            return []
        l = self.getKthSmallest(root.left)
        r = self.getKthSmallest(root.right)
        return [*l, root.val, *r]
# Second solution (beats 100%)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        _, ret = self.getKthSmallest(root, k)
        return ret

    def getKthSmallest(self, root: Optional[TreeNode], k:int) -> Tuple[int, Optional[int]]:
        if root is None:
            return 0, None
        l, ret = self.getKthSmallest(root.left, k)
        if ret is not None:
            return k, ret
        elif l+1 == k:
            return k, root.val
        r, ret = self.getKthSmallest(root.right, k - l - 1)
        if ret is not None:
            return k, ret
        return l+r+1, None
