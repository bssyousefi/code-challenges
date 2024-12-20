// First solution (beats 35%) (merge one by one)
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    if len(lists) == 0 {
        return nil
    }
    res := lists[0]

    for i:=1;i<len(lists);i++ {
        res = merge2Lists(res, lists[i])
    }
    return res
}

func merge2Lists(l1, l2 *ListNode) *ListNode {
    head := &ListNode{}
    cur := head

    for l1 != nil || l2 != nil {
        if l1 != nil && l2 != nil {
            if l1.Val < l2.Val {
                cur.Next = l1
                l1 = l1.Next
            } else {
                cur.Next = l2
                l2 = l2.Next
            }
        } else if l1 != nil {
            cur.Next = l1
            break
        } else {
            cur.Next = l2
            break
        }
        cur = cur.Next
    }
    return head.Next
}
// Second solution (beats 100%) (use default sort)
func mergeKLists(lists []*ListNode) *ListNode {
    l := make([]int,0)
    for _, i := range lists {
        for i != nil {
            l = append(l, i.Val)
            i = i.Next
        }
    }
    slices.Sort(l)
    head := &ListNode{}
    cur := head
    for _, i := range l {
        cur.Next = &ListNode{Val:i}
        cur = cur.Next
    }
    return head.Next
}
