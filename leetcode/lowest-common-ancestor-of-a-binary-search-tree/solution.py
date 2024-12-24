# First solution (beats 24%) (ignored BST)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret, _ = self.hasSubNodes(root, p, q)
        return ret

    def hasSubNodes(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Tuple[Optional['TreeNode'],int]:
        if root is None:
            return None, 0
        ret = 0
        if root == p or root == q:
            ret += 1

        lr, l = self.hasSubNodes(root.left, p, q)
        rr, r = self.hasSubNodes(root.right, p, q)
        if lr:
            return lr, 2
        if rr:
            return rr, 2
        if ret+l+r == 2:
            return root, 2
        else:
            return None, ret+l+r
# Second solution (beats 67%)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        cur = root
        while cur:
            if cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right
            else:
                return cur
# Third solution (beats 88%)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
