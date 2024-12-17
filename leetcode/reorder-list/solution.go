// First solution (beats 100%)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    cur := head
    l := []*ListNode{}
    for cur != nil {
        l = append(l, cur)
        cur = cur.Next
    }
    m := len(l)
    if m < 3 {
        return
    }
    count := 0
    cur = head
    for i:=0;i<(m/2);i++ {
        if i != 0 {
            cur = cur.Next.Next
        }
        tmp := cur.Next
        cur.Next = l[m-1-count]
        cur.Next.Next = tmp
        count++ 
    }
    if m % 2 == 0 {
        cur.Next.Next = nil
    } else {
        cur.Next.Next.Next = nil
    }
}
