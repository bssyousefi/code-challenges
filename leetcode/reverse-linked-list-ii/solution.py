# First solution (beats 100%) (stack)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = ListNode(0, head)
        new_head = cur
        counter = 0
        while cur and cur.next:
            if counter + 1 == left:
                stack = []
                moving = cur.next
                counter += 1
                while moving:
                    stack.append(moving)
                    if counter == right:
                        end = moving.next
                        break
                    moving = moving.next
                    counter += 1
                while stack:
                    cur.next = stack.pop()
                    cur = cur.next
                cur.next = end
                break
            else:
                cur = cur.next
            counter += 1

        return new_head.next
