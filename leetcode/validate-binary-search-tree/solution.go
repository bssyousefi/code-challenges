// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    if root == nil {
        return true
    }
    return isValidBst(root, -1<<31 - 1, 1<<31)
}

func isValidBst(root *TreeNode, min_ int, max_ int) bool {
    if root == nil {
        return true
    }
    if root.Val <= min_ {
        return false
    }
    if root.Val >= max_ {
        return false
    }

    ret := isValidBst(root.Left, min_, root.Val)
    ret = ret && isValidBst(root.Right, root.Val, max_)
    return ret
}
