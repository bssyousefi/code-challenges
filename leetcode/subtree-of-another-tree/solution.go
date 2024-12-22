// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if root == nil {
        if subRoot == nil {
            return true
        } else {
            return false
        }
    }
    if isSameTree(root, subRoot) {
        return true
    }
    if isSubtree(root.Left, subRoot) {
        return true
    }
    return isSubtree(root.Right, subRoot)
}

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
