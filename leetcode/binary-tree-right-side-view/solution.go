// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    q := []*TreeNode{root}
    res := []int{}
    var tmp int
    for len(q) != 0 {
        l := len(q)
        for i:=0;i<l;i++ {
            if q[i] != nil {
                tmp = q[i].Val
                if q[i].Left != nil {
                    q = append(q, q[i].Left)
                }
                if q[i].Right != nil {
                    q = append(q, q[i].Right)
                }
            }
        }
        q = q[l:]
        res = append(res, tmp)
    }
    return res
}
