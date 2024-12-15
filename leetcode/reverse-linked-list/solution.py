# First solution (beats 100%)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            node = ListNode(head.val, node)
            head = head.next

        return node
