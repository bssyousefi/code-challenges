# First solution (beats 100%)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        tmp = []
        q.append((root,0))
        l_pre = None
        while q:
            node, l = q.popleft()
            if l != l_pre:
                if l_pre is not None:
                    res.append(tmp)
                l_pre = l
                tmp = []
            if node:
                q.append((node.left, l+1))
                q.append((node.right, l+1))
                tmp.append(node.val)
        return res

# Second solution (beats 100%)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        ret = []
        i = 0

        while queue:
            group = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    group.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            ret.append(group)

        return ret

