// First solution (beats 100%) (DFS)
func numIslands(grid [][]byte) int {
    ret := 0
    rows := len(grid)
    cols := len(grid[0])
    var dfs func(int, int)
    dfs = func(i int, j int) {
        grid[i][j] = '0'
        if i < rows-1 && grid[i+1][j] == '1' {
            dfs(i+1, j)
        }
        if j < cols-1 && grid[i][j+1] == '1' {
            dfs(i, j+1)
        }
        if i > 0 && grid[i-1][j] == '1' {
            dfs(i-1, j)
        }
        if j > 0 && grid[i][j-1] == '1' {
            dfs(i, j-1)
        }
    }
    for i:=0;i<rows;i++ {
        for j:=0;j<cols;j++ {
            if grid[i][j] == '1' {
                ret++
                dfs(i, j)
            }
        }
    }
    return ret
}
