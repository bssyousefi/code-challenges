// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
    _, m := diameterOfBinaryTreeCalc(root)
    return m
}
func diameterOfBinaryTreeCalc(root *TreeNode) (int, int) {
    if root == nil {
        return 0, 0
    }
    if root.Left == nil && root.Right == nil {
        return 1, 0
    }
    l, r, lMax, rMax := 0, 0, 0, 0
    if root.Left != nil {
        l, lMax = diameterOfBinaryTreeCalc(root.Left)
    }
    if root.Right != nil {
        r, rMax = diameterOfBinaryTreeCalc(root.Right)
    }

    return max(l,r) + 1, max(lMax, rMax, r+l)
}
