# First solution (beats 81%)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ret = str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        return ret


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        A = data.split(",")
        A.reverse()
        return self.deserializeList(A)

    def deserializeList(self, data):
        val = data.pop()
        if val == "":
            return None
        root = TreeNode(val)
        root.left = self.deserializeList(data)
        root.right = self.deserializeList(data)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
