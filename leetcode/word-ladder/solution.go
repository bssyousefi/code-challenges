// First solution (beats 97%) (BFS + Brute-force + from two ends)
func ladderLength(beginWord string, endWord string, wordList []string) int {
    words := map[string]bool{}
    s1 := map[string]int{beginWord: 1}
    s2 := map[string]int{endWord: 1}
    for _, i := range wordList {
        words[i] = true
    }
    if !words[endWord] {
        return 0
    }
    // words[endWord] = false
    // words[beginWord] = false

    q1 := []string{beginWord}
    q2 := []string{endWord}
    for len(q1)>0 && len(q2)>0 {
        if len(q1) > len(q2) {
            s1, s2 = s2, s1
            q1, q2 = q2, q1
        }
        m := len(q1)
        for n:=0;n<m;n++ {
            i := q1[0]
            q1 = q1[1:]
            if s2[i] > 0 {
                fmt.Printf("%v and %v\n", s1, s2)
                return s2[i] + s1[i] - 1
            }
            for k:=0;k<len(i);k++ {
                for j:=97;j<123;j++ {
                    tmp := i[:k] + string(byte(j)) + i[k+1:]
                    if words[tmp] && s1[tmp] == 0{
                        s1[tmp] = s1[i] + 1
                        q1 = append(q1, tmp)
                    }
                }
            }
        }
    }
    return 0
}
