// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    _max := 0
    if root.Left != nil {
        _max = max(_max, maxDepth(root.Left))
    }
    if root.Right != nil {
        _max = max(_max, maxDepth(root.Right))
    }
    return _max + 1
}
