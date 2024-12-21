// First solution (beats 100%)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
    l := []*ListNode{}
    mainHead := &ListNode{Next:head}
    pre := mainHead
    for head != nil {
        l = append(l, head)
        head = head.Next
        if len(l) == k {
            for len(l) != 0 {
                pre.Next = l[len(l)-1]
                l = l[:len(l)-1]
                pre = pre.Next
            }
            pre.Next = head
        }
    }
    return mainHead.Next
}
