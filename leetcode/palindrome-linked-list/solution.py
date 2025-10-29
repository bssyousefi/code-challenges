# First solution (beats 75%)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        ll = len(l)
        for i in range(ll//2):
            if l[i] != l[ll-i-1]:
                return False

        return True

