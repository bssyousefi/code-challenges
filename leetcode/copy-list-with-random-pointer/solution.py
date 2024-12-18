# First solution (beats 5%)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        l = []
        n, m = [], []
        while cur:
            l.append(cur)
            n.append(cur.random)
            cur = cur.next

        for i in range(len(n)):
            for j in range(len(l)):
                if n[i] == l[j]:
                    m.append(j)
                    break
            if len(m) == i:
                m.append(-1)

        i = len(l) - 1
        k = []
        pre = None
        while i >= 0:
            pre = Node(l[i].val, pre)
            k.insert(0, pre)
            i -= 1

        i = 0
        head = pre
        while i < len(k):
            if m[i] == -1:
                pre.random = None
            else:
                pre.random = k[m[i]]
            pre = pre.next
            i += 1

        return head
# Second solution (beats 5%)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        l = []
        n, m = [], []
        count = 0
        while cur:
            l.append(cur)
            if cur.random:
                n.append((count, cur.random))
            cur = cur.next
            count += 1

        for i in range(len(n)):
            for j in range(len(l)):
                if n[i][1] == l[j]:
                    m.append((n[i][0], j))
                    break

        i = len(l) - 1
        k = []
        pre = None
        while i >= 0:
            pre = Node(l[i].val, pre)
            k.insert(0, pre)
            i -= 1

        i = 0
        while i < len(m):
            k[m[i][0]].random = k[m[i][1]]
            i += 1

        return pre
# Second solution (beats 86%)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur:
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            tmp = cur.next.next
            if tmp:
                cur.next.next = tmp.next
            cur = tmp

        return head.next if head else head
