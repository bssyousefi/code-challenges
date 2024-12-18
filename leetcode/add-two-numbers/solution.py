# First solution (beats 100%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        ret = 0
        while l1 or l2 or ret:
            v = ret
            if l1 and l2:
                v += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                v += l1.val
                l1 = l1.next
            elif l2:
                v += l2.val
                l2 = l2.next

            if v >= 10:
                ret = 1
                v = v - 10
            else:
                ret = 0
            cur.next = ListNode(v)
            cur = cur.next

        return head.next
