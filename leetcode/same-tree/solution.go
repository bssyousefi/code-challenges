// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p != nil && q != nil {
        if p.Val != q.Val {
            return false
        }
        l := isSameTree(p.Left, q.Left)
        r := isSameTree(p.Right, q.Right)
        return l && r
    } else if p == nil && q == nil {
        return true
    } else {
        return false
    }
}
