// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {
    ret, _ := getMaxPathSum(root)
    return ret
}

func getMaxPathSum(root *TreeNode) (int, int) {
    if root == nil {
        return 0, 0
    }
    if root.Left == nil && root.Right == nil {
        return root.Val, root.Val
    }

    m := root.Val
    l, r, la, ra := 0, 0, 0, 0
    if root.Left != nil {
        l, la = getMaxPathSum(root.Left)
        if l > m {
            m = l
        }
    }
    if root.Right != nil {
        r, ra = getMaxPathSum(root.Right)
        if r > m {
            m = r
        }
    }
    return max(m, max(ra, la, ra+la) + root.Val), max(ra, la, 0) + root.Val
}
