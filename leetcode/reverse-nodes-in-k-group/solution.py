# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        h = ListNode()
        h.next = head
        i = h
        
        while i:
            c = 0
            j = i
            while c < k:
                if j.next:
                    j = j.next
                else:
                    i = None
                    break
                c += 1
            if c == k:
                i = self.reverse(i,j)
        return h.next

    def reverse(self, s, e):
        p = e.next
        pre = s
        cur = s.next
        b = cur
        
        while cur != e:
            next = cur.next
            cur.next = p
            p = cur
            cur = next
        cur.next = p
        pre.next = cur

        return b
