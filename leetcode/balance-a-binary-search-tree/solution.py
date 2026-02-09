# First solution (beats 47%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            values.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)

        def create(vals):
            l = len(vals)
            if l == 1:
                return TreeNode(vals[0])
            elif l == 2:
                return TreeNode(vals[0], right=TreeNode(vals[1]))
            else:
                left = create(vals[:l//2])
                right = create(vals[l//2+1:])
                return TreeNode(vals[l//2], left=left, right=right)

        return create(values)
