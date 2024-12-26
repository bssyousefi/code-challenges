// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
    _, ret := getKthSmallest(root, k)
    return ret.Val
}

func getKthSmallest(root *TreeNode, k int) (int, *TreeNode) {
    if root == nil {
        return 0, nil
    }
    l, ret := getKthSmallest(root.Left, k)
    if ret != nil {
        return k, ret
    }
    if l + 1 == k {
        return k, root
    }
    r , ret := getKthSmallest(root.Right, k - l - 1)
    if ret != nil {
        return k, ret
    }
    return l + r + 1, nil
}
