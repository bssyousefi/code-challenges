// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isBalanced(root *TreeNode) bool {
    _, m := checkBalance(root)
    return m   
}

func checkBalance(root *TreeNode) (int, bool) {
    if root == nil {
        return 0, true
    }
    l, lB := checkBalance(root.Left)
    r, rB := checkBalance(root.Right)

    return max(l,r) + 1, lB && rB && math.Abs(float64(l-r)) < 2
}
