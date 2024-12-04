// First solution (beats 100%)
func generateParenthesis(n int) []string {
    type Node struct {
        Open   int
        Close   int
        Text   string
    }
    ret := []string{}
    q := []Node{Node{n-1, n, "("}}
    for len(q) > 0 {
        n := q[0]
        q = q[1:]
        if n.Open > 0 {
            q = append(q, Node{n.Open-1, n.Close, n.Text + "("})
        } else if n.Close == 0 {
            ret = append(ret, n.Text)
        }
        if n.Close > 0 && n.Close > n.Open {
            q = append(q, Node{n.Open, n.Close-1, n.Text + ")"})
        }
    }
    return ret
}
