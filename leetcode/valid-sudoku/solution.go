// First Solution (beats 100%, but seems messy code)
func isValidSudoku(board [][]byte) bool {
    _map := make(map[int]map[byte]bool)
    for i:=0; i<9; i++ {
        s := map[byte]bool{}
        for j:=0; j<9; j++ {
            v := board[i][j]
            if v == '.' {
                continue
            }
            if _, ok := s[v]; ok {
                return false
            } else {
                s[v] = true
            }
            if _, ok := _map[j][v]; ok {
                return false
            } else {
                if _map[j] == nil {
                    _map[j] = make(map[byte]bool)
                }
                _map[j][v] = true
            }
            if _, ok := _map[10*(i/3)+(j/3)+10][v]; ok {
                return false
            } else {
                if _map[10*(i/3)+(j/3)+10] == nil {
                    _map[10*(i/3)+(j/3)+10] = make(map[byte]bool)
                }
                _map[10*(i/3)+(j/3)+10][v] = true
            }
        }
    }
    return true
}
