// First solution (beats 84%)
func exist(board [][]byte, word string) bool {
    rows := len(board)
    cols := len(board[0])
    var dfs func(i, j, k int) bool
    dfs = func(i, j, k int) bool {
        if (
            i < 0 || i == rows ||
            j < 0 || j == cols ||
            board[i][j] != word[k]) {
            return false
        }
        if k == len(word)-1 {
            return true
        }
        tmp := board[i][j]
        board[i][j] = '#'
        ret := (
            dfs(i-1, j, k+1) ||
            dfs(i+1, j, k+1) ||
            dfs(i, j-1, k+1) ||
            dfs(i, j+1, k+1))
        board[i][j] = tmp
        return ret
    }
    for i := range board {
        for j := range board[i] {
            if dfs(i, j, 0) {
                return true
            }
        }
    }
    return false
}
