// First solution (beats 100%) (DFS)
func solve(board [][]byte)  {
    rows := len(board)
    cols := len(board[0])
    d := make([][]bool,rows)
    for i, _ := range d {
        d[i] = make([]bool, cols)
    }
    drx := [4][2]int{[2]int{-1,0},[2]int{0,-1},[2]int{1,0},[2]int{0,1}}
    var cal func (i,j int)
    cal = func (i,j int) {
        if i < 0 || j < 0 || i==rows || j==cols || d[i][j] || board[i][j] == 'X' {
            return
        }
        d[i][j] = true
        for _, v := range drx {
            cal(i+v[0], j+v[1])
        }
    }
    for i:=0;i<rows;i++ {
        if board[i][0] == 'O' {
            cal(i,0)
        }
        if board[i][cols-1] == 'O' {
            cal(i,cols-1)
        }
    }
    for i:=0;i<cols;i++ {
        if board[0][i] == 'O' {
            cal(0,i)
        }
        if board[rows-1][i] == 'O' {
            cal(rows-1,i)
        }
    }
    for i:=0;i<rows;i++ {
        for j:=0;j<cols;j++ {
            if board[i][j] == 'O' && !d[i][j] {
                board[i][j] = 'X'
            }
        }
    }
}
