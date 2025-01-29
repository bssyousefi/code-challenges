// First solution (beats 100%) (DFS)
func findOrder(numCourses int, prerequisites [][]int) []int {
    visit := make([]bool, numCourses)
    tmp := make([]bool, numCourses)
    ret := []int{}
    d := map[int][]int{}
    for _, v := range prerequisites {
        d[v[0]] = append(d[v[0]], v[1])
    }

    var dfs func(int) bool
    dfs = func(i int) bool {
        if visit[i] {
            return true
        }
        if tmp[i] {
            return false
        }
        tmp[i] = true
        for _, v := range d[i] {
            if !dfs(v) {
                return false
            }
        }
        ret = append(ret, i)
        visit[i] = true
        return true
    }

    for i:=0;i<numCourses;i++ {
        if !visit[i] {
            if !dfs(i) {
                return []int{}
            }
        }
    }
    return ret
}
