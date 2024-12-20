# First solution (beats 8%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Head:
            def __init__(self, node: ListNode = None, left: ListNode = None, right: ListNode = None):
                self.left = left
                self.right = right
                self.node = node

        def find_and_replace(head: Head, node: Head):
            if head.left is None:
                head.left, head.right = node, node
                node.left, node.right = head
                return
            cur = head.right
            while cur != head and node.node.val > cur.node.val:
                cur = cur.right
            cur.left.right, node.left = node, cur.left
            cur.left, node.right = node, cur
            return

        head = Head()
        head.left, head.right = head, head
        for node in lists:
            if node:
                cur = Head(node)
                find_and_replace(head, cur)

        res = ListNode()
        cur = res
        _min = 1e5
        while head.right.node:
            right = head.right
            node = head.right.node
            cur.next = node
            node = node.next
            head.right.right.left = head
            head.right = head.right.right
            if node:
                right.node = node
                find_and_replace(head, right)
            cur = cur.next

        return res.next
# Second solution (beats 99%) (use default sort)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        _min = 1e5
        new_list = []
        for i in lists:
            while i:
                new_list.append(i.val)
                i = i.next

        for i in sorted(new_list):
            cur.next = ListNode(i)
            cur = cur.next

        return res.next
# Third solution (beats 11%) (merge one by one)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        res = lists[0]

        for i in range(1,len(lists)):
            res = self.merge_lists(res, lists[i])

        return res

    def merge_lists(self, l1, l2):
        head = ListNode()
        cur = head
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            elif l1:
                cur.next = l1
                break
            else:
                cur.next = l2
                break
            cur = cur.next
        return head.next
