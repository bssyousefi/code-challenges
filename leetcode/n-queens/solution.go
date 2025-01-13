// First solution (beats 100%)
func solveNQueens(n int) [][]string {
    cols := map[int]bool{}
    sums := map[int]bool{}
    subs := map[int]bool{}

    ret := [][]string{}
    board := make([][]byte, n)
    var tmp []string{}

    for i:=0; i<n; i++ {
        board[i] = make([]byte, n)
        for j:=0;j<n;j++ {
            board[i][j] = '.'
        }
    }

    var cal func(m int)
    cal = func(m int) {
        if m == -1 {
            tmp = []string{}
            for _, v := range board {
                tmp = append(tmp, string(v))
            }
            ret = append(ret, tmp)
        }
        for i:=0;i<n;i++ {
            if cols[i] || sums[i+m] || subs[i-m] {
                continue
            }
            cols[i] = true
            sums[i+m] = true
            subs[i-m] = true
            board[m][i] = byte('Q')
            cal(m-1)
            board[m][i] = byte('.')
            subs[i-m] = false
            sums[i+m] = false
            cols[i] = false
        }
    }

    cal(n-1)

    return ret
}
