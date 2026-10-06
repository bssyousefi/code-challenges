# First solution (beats 100%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next
        cur = head
        m = len(l)
        if len(l) < 3:
            return
        count = len(l) // 2
        for i in range(count):
            if i > 0:
                cur = cur.next.next
            tmp = cur.next
            cur.next = l.pop()
            cur.next.next = tmp

        if m % 2 == 0:
            cur.next.next = None
        else:
            cur.next.next.next = None

# Second solution (beats 16%)
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head

        def dfs(node):
            nonlocal cur
            if node and node.next and node.next.next:
                if dfs(node.next):
                    return True
            if cur == node or node.next.next == cur:
                return True
            else:
                cur.next, node.next.next, node.next = node.next, cur.next, None
                cur = cur.next.next
                return False

        dfs(head)
