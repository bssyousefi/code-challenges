# First solution (beats 91%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.visited = set()
        return self.getTree()

    def getTree(self):
        if len(self.preorder) == 0:
            return None
        root = TreeNode(self.preorder.pop(0))
        self.visited.add(root.val)

        if self.inorder[0] == root.val:
            self.inorder.pop(0)
        else:
            root.left = self.getTree()
            self.inorder.pop(0)

        if len(self.inorder) == 0 or self.inorder[0] in self.visited:
            return root
        root.right = self.getTree()

        return root
# Second solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        return self.getTree(None)

    def getTree(self,val):
        if self.inorder and self.inorder[0] != val:
            root = TreeNode(self.preorder.pop(0))
            root.left = self.getTree(root.val)
            self.inorder.pop(0)
            root.right = self.getTree(val)
            return root
        else:
            return None
