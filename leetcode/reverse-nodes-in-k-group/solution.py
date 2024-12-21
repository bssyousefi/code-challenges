# Old solution
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
# First solution (beats 100%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        main_head = ListNode(0, head)
        pre = main_head
        while head:
            l.append(head)
            head = head.next
            if len(l) == k:
                while l:
                    pre.next = l.pop()
                    pre = pre.next
                pre.next = head

        return main_head.next
