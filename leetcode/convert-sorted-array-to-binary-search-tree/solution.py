# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        if l == 1:
            return TreeNode(nums[0])

        root = TreeNode(nums[l//2])
        root.left = self.sortedArrayToBST(nums[:l//2])
        if l > 2:
            root.right = self.sortedArrayToBST(nums[l//2+1:])
        return root

