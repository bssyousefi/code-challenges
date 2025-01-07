// Solution (beats 91%)
type Trie struct {
    children [26]*Trie
    end      bool
}

func (t *Trie) addWord(word string) {
    if word == "" {
        t.end = true
        return
    }
    idx := word[0] - 'a'
    if t.children[idx] == nil {
        t.children[idx] = &Trie{}
    }
    t.children[idx].addWord(word[1:])
}
func findWords(board [][]byte, words []string) []string {
    rows := len(board)
    cols := len(board[0])
    root := &Trie{}
    for _, word := range words {
        root.addWord(word)
    }
    ret := []string{}
    var dfs func(int, int, *Trie, string)
    dfs = func(i int, j int, node *Trie, word string) {
        if board[i][j] == '#' {
            return 
        }
        idx := board[i][j] - 'a'
        if node.children[idx] == nil {
            return
        }
        root := node.children[idx]
        word += string(byte('a'+idx))
        if root.end {
            ret = append(ret, word)
            root.end = false
        }
        board[i][j] = '#'
        if i > 0 {
            dfs(i-1, j, root, word)
        }
        if i < (rows - 1) {
            dfs(i+1, j, root, word)
        }
        if j > 0 {
            dfs(i, j-1, root, word)
        }
        if j < (cols - 1) {
            dfs(i, j+1, root, word)
        }
        board[i][j] = byte(idx+'a')
        if root.children == [26]*Trie{} {
            node.children[idx] = nil
        }
    }
    for i := range board {
        for j := range board[i] {
            dfs(i, j, root, "")
        }
    }
    return ret
}
