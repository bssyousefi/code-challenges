// First solution (beats 99%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
    return getCountOfGoodNodes(root, root.Val)
}

func getCountOfGoodNodes(root *TreeNode, max_ int) int{
    if root == nil {
        return 0
    }
    ret := 0
    if root.Val >= max_ {
        max_ = root.Val
        ret += 1
    }
    ret += getCountOfGoodNodes(root.Left, max_)
    ret += getCountOfGoodNodes(root.Right, max_)
    return ret
}
