// First solution (beats 100%)
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    cur := head
    for cur != nil {
        node := &Node{cur.Val, cur.Next, nil}
        cur.Next = node
        cur = node.Next
    }
    cur = head
    for cur != nil {
        if cur.Random != nil {
            cur.Next.Random = cur.Random.Next
        }
        cur = cur.Next.Next
    }
    newHead := head.Next
    newCur := newHead
    cur = head
    for cur != nil {
        cur.Next = newCur.Next
        if cur.Next != nil {
            newCur.Next = cur.Next.Next
            newCur = newCur.Next
        }
        cur = cur.Next
    }
    return newHead
}
