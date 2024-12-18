// First solution (beats 100%)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := &ListNode{}
    cur := head
    ret := 0
    for l1 != nil || l2 != nil || ret != 0 {
        v := ret
        if l1 != nil && l2 != nil {
            v += l1.Val + l2.Val
            l1 = l1.Next
            l2 = l2.Next
        } else if l1 != nil {
            v += l1.Val
            l1 = l1.Next
        } else if l2 != nil {
            v += l2.Val
            l2 = l2.Next
        }
        if v >= 10 {
            ret = 1
            v -= 10
        } else {
            ret = 0
        }
        cur.Next = &ListNode{v,nil}
        cur = cur.Next
    }
    return head.Next
}
