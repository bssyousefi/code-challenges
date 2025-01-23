// First solution (beats 50%) (DFS, flow upward)
func pacificAtlantic(heights [][]int) [][]int {
    rows := len(heights)
    cols := len(heights[0])
    visitP := map[[2]int]bool{}
    visitA := map[[2]int]bool{}
    dx := [4][2]int{[2]int{-1,0},[2]int{0,-1},[2]int{1,0},[2]int{0,1}}
    ret := [][]int{}
    var flowUp func(i,j int, v map[[2]int]bool)


    flowUp = func(i,j int, v map[[2]int]bool) {
        v[[2]int{i,j}] = true
        for _, m := range dx {
            r,c := i+m[0], j+m[1]
            if r < 0 || r == rows || c < 0 || c == cols || v[[2]int{r,c}] || heights[r][c] < heights[i][j] {
                continue
            }
            flowUp(r,c,v)
        }
    }

    for i:=0;i<rows;i++ {
        flowUp(i,0,visitP)
        flowUp(i,cols-1,visitA)
    }
    for i:=0;i<cols;i++ {
        flowUp(0,i,visitP)
        flowUp(rows-1,i,visitA)
    }
    for i, _ := range visitP {
        if visitA[i] {
            ret = append(ret, []int{i[0], i[1]})
        }
    }
    return ret
}
// Second solution (beats 100%) (DFS, flow upward, array instead of map)
func pacificAtlantic(heights [][]int) [][]int {
    rows := len(heights)
    cols := len(heights[0])
    visitP := make([][]bool, 0, rows)
    visitA := make([][]bool, 0, rows)
    for i:=0;i<rows;i++ {
        visitP = append(visitP, make([]bool, cols))
        visitA = append(visitA, make([]bool, cols))
    }

    dx := [4][2]int{[2]int{-1,0},[2]int{0,-1},[2]int{1,0},[2]int{0,1}}
    ret := [][]int{}
    var flowUp func(i,j int, v [][]bool)


    flowUp = func(i,j int, v [][]bool) {
        v[i][j] = true

        for _, m := range dx {
            r,c := i+m[0], j+m[1]
            if r < 0 || r == rows || c < 0 || c == cols || v[r][c] || heights[r][c] < heights[i][j] {
                continue
            }
            flowUp(r,c,v)
        }
    }

    for i:=0;i<rows;i++ {
        flowUp(i,0,visitP)
        flowUp(i,cols-1,visitA)
    }
    for i:=0;i<cols;i++ {
        flowUp(0,i,visitP)
        flowUp(rows-1,i,visitA)
    }
    for i:=0;i<rows;i++ {
        for j:=0;j<cols;j++ {
            if visitP[i][j] && visitA[i][j] {
                ret = append(ret, []int{i,j})
            }
        }
    }
    return ret
}
