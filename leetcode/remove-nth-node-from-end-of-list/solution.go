// First solution (beats 100%)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    cur := head
    l := []*ListNode{}
    for cur != nil {
        l = append(l, cur)
        cur = cur.Next
    }

    node := l[len(l)-n]
    cur = head

    for cur != node {
        if cur.Next == node {
            cur.Next = node.Next
            break
        }
        cur = cur.Next
    }
    if cur == node {
        head = head.Next
    }
    return head
}
