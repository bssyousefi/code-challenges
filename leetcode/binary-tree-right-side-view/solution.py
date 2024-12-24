# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ret = []
        while q:
            tmp = None
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                if node:
                    tmp = node.val
                    q.append(node.left)
                    q.append(node.right)
            if tmp is not None:
                ret.append(tmp)

        return ret
