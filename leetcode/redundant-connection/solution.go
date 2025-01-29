// First solution (beats 100%) (DFS)
func findRedundantConnection(edges [][]int) []int {
    d := map[int][]int{}
    for _, v := range edges {
        d[v[0]] = append(d[v[0]], v[1])
        d[v[1]] = append(d[v[1]], v[0])
    }
    visit := make([]bool, len(d))
    loop := map[int]bool{}

    var dfs func (int, int) int
    dfs = func(i, j int) int {
        visit[i-1] = true
        for _, v := range d[i] {
            if v != j {
                if visit[v-1] {
                    loop[v] = true
                    return v
                }
                ret := dfs(v, i) 
                if ret == 0 {
                    return 0
                } else if ret > 0 {
                    loop[v] = true
                    if ret == i {
                        return 0
                    }
                    return ret
                }
            }
        }
        return -1
    }
    for i:=1;i<=len(d);i++ {
        if !visit[i-1] {
            if dfs(i,-1) == 0 {
                break
            }
        }
    }

    for i:=len(edges)-1;i>-1;i-- {
        if loop[edges[i][0]] && loop[edges[i][1]] {
            return edges[i]
        }
    }
    return []int{}
}
