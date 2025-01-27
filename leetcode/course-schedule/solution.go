// First solution (beats 70%) (DFS)
func canFinish(numCourses int, prerequisites [][]int) bool {
    d := map[int][]int{}
    visit := map[int]bool{}
    tmp := map[int]bool{}

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
        for _, j := range d[i] {
            if !dfs(j) {
                return false
            }
        }
        visit[i] = true
        return true
    }

    for i:=0;i<numCourses;i++ {
        if !dfs(i) {
            return false
        }
    }
    return true
}
// Second solution (beats 100%) (DFS) (use slice instead of map)
func canFinish(numCourses int, prerequisites [][]int) bool {
    d := make([][]int,numCourses)
    visit := make([]bool,numCourses)
    tmp := make([]bool, numCourses)

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
        for _, j := range d[i] {
            if !dfs(j) {
                return false
            }
        }
        visit[i] = true
        return true
    }

    for i:=0;i<numCourses;i++ {
        if !dfs(i) {
            return false
        }
    }
    return true
}
