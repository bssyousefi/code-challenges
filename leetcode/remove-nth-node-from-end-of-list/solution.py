# First solution (beats 100%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        l = []
        while cur:
            l.append(cur)
            cur = cur.next

        node = l[-n]

        cur = head
        while cur != node:
            if cur.next == node:
                cur.next = node.next
                break
            cur = cur.next
        else:
            head = cur.next

        return head
