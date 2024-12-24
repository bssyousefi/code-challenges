// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    q := []*TreeNode{root}
    res := [][]int{}
    for len(q) != 0 {
        tmp := []int{}
        l := len(q)
        for i:=0;i<l;i++ {
            if q[i] != nil {
                tmp = append(tmp, q[i].Val)
                q = append(q, q[i].Left)
                q = append(q, q[i].Right)
            }
        }
        q = q[l:]
        if len(tmp) > 0 {
            res = append(res, tmp)
        }
    }
    return res
}
