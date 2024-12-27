// First solution (beats 100%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
   return getTree(&preorder, &inorder, nil)
}

func getTree(preorder *[]int, inorder *[]int, val *int) *TreeNode{
    if len(*preorder) > 0 && len(*inorder) > 0 && (val == nil || (*inorder)[0] != *val) {
        root := &TreeNode{Val:(*preorder)[0]}
        *preorder = (*preorder)[1:]
        root.Left = getTree(preorder, inorder, &root.Val)
        *inorder = (*inorder)[1:]
        root.Right = getTree(preorder, inorder, val)
        return root
    }
    return nil
}
