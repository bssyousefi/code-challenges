// First solution (beats 100%)
func partitionLabels(s string) []int {
    m := map[byte]int{}
    for i:=0;i<len(s);i++ {
        m[s[i]] = i
    }

    start := 0
    end := 0
    ret := []int{}

    for i:=0;i<len(s);i++ {
        if end < m[s[i]] {
            end = m[s[i]]
        }
        if i == end {
            ret = append(ret, end-start+1)
            start = i + 1
        }
    }
    return ret
}
// Second solution (beats 32%)
func partitionLabels(s string) []int {
    m := map[byte]int{}
    for i:=0;i<len(s);i++ {
        m[s[i]]++
    }

    start := 0
    c := map[byte]bool{}
    ret := []int{}

    for i:=0;i<len(s);i++ {
        c[s[i]] = true
        m[s[i]]--
        if m[s[i]] == 0 {
            delete(c, s[i])
            if len(c) == 0 {
                ret = append(ret, i-start+1)
                start = i + 1
            }
        }
    }
    return ret
}
