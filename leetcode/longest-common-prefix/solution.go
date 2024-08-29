func longestCommonPrefix(strs []string) string {
    s := make([]byte,1)
    i := 0
    r := byte(0)
    j := 0
    l := len(strs)
    if l == 1 {
        return strs[0]
    }
    for true {
        if i == len(strs[0]) {
            break
        }
        r = strs[0][i]
        j = 1
        for j < l {
            if i >= len(strs[j]) || strs[j][i] != r {
                break
            }
            j++
        }
        if j != l {
            break
        }
        s = append(s, r)
        i++
    }
    return string(s[1:])
}
