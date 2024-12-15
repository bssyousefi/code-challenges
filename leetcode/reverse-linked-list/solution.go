// First solution (beats 100%)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var node *ListNode
    for head != nil {
        node = &ListNode{head.Val, node}
        head = head.Next
    }
    return node
}
