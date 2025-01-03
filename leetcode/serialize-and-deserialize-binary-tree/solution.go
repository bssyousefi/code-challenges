// First solution (beats 54%)
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
    
}

func Constructor() Codec {
    return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
    if root == nil {
        return ""
    }
    return fmt.Sprintf("%d,%s,%s", root.Val, this.serialize(root.Left), this.serialize(root.Right))
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {    
    A := strings.Split(data, ",")
    root, _ := this.deserializeSlice(A, 0)
    return root
}

func (this *Codec) deserializeSlice(data []string, i int) (*TreeNode, int) {
    if data[i] == "" {
        return nil, i+1
    }
    j := i
    val, _ := strconv.ParseInt(data[i], 10, 0)
    root := &TreeNode{Val: int(val)}
    root.Left, j = this.deserializeSlice(data, i+1)
    root.Right, j = this.deserializeSlice(data, j)
    return root, j
}


/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
