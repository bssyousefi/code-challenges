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

# Second solution (beats 83%) (basically the same)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, _max) -> int:
            count = 0
            if node is None:
                return count
            if node.val >= _max:
                count += 1
            new_max = max(_max, node.val)
            return count + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)
