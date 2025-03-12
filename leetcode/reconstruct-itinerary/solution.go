// First solution (beats 100%) (DFS)
func findItinerary(tickets [][]string) []string {
    slices.SortFunc(tickets, func (a, b []string) int {
        if a[0] < b[0] {
            return -1
        } else if a[0] > b[0] {
            return 1
        } else if a[1] < b[1] {
            return -1
        } else if a[1] > b[1] {
            return 1
        } else {
            return 0
        }
    })
    m := map[string][]string{}
    for i:=len(tickets)-1;i>=0;i-- {
        m[tickets[i][0]] = append(m[tickets[i][0]], tickets[i][1])
    }
    ret := []string{}
    var dfs func(string)
    dfs = func(i string) {
        for len(m[i]) > 0 {
            arg := m[i][len(m[i])-1]
            m[i] = m[i][:len(m[i])-1]
            dfs(arg)
        }
        ret = append(ret, i)
    }
    dfs("JFK")
    l := len(ret)
    for i:=0;i<(l/2);i++ {
        ret[i], ret[l-1-i] = ret[l-1-i], ret[i]
    }
    return ret
}
