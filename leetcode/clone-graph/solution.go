// First solution (beats 100%) (DFS)
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    d := map[*Node]*Node{}
    var dfs func(*Node) *Node
    dfs = func(n *Node) *Node {
        if n == nil {
            return nil
        }
        if _, ok := d[n]; ok {
            return d[n]
        }
        d[n] = &Node{Val: n.Val}
        for _, i := range n.Neighbors {
            d[n].Neighbors = append(d[n].Neighbors, dfs(i))
        }
        return d[n]
    }
    return dfs(node)
}
