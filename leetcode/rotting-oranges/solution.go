// First solution (beats 100%) (BFS)
func orangesRotting(grid [][]int) int {
    q := [][2]int{}
    fresh := 0
    rows := len(grid)
    cols := len(grid[0])
    for i:=0;i<rows;i++ {
        for j:=0;j<cols;j++ {
            if grid[i][j] == 1 {
                fresh++
            }
            if grid[i][j] == 2 {
                q = append(q, [2]int{i, j})
            }
        }
    }
    directions := [4][2]int{[2]int{-1,0},[2]int{0,-1},[2]int{1,0},[2]int{0,1}}
    times := 0
    for fresh > 0 && len(q) > 0 {
        for _ = range q {
            r, c := q[0][0], q[0][1]
            q = q[1:]
            for _, i := range directions {
                if r+i[0] < 0 || r+i[0] == rows || c+i[1] < 0 || c+i[1] == cols || grid[r+i[0]][c+i[1]] != 1 {
                    continue
                }
                grid[r+i[0]][c+i[1]] = 2
                fresh--
                q = append(q, [2]int{r+i[0], c+i[1]})
            }
        }
        times++
    }
    if fresh > 0 {
        return -1
    } else {
        return times
    }
}
