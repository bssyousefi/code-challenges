// First solution (beats 100%) (two pointers)
func longestPalindrome(s string) string {
    if len(s) == 0 {
        return s
    }
    max_ := 1
    start := 0
    var check func (int, int)

    check = func (i, j int) {
        for i>0 && j < len(s)-1 && s[i-1] == s[j+1] {
            i--
            j++
        }
        if j-i+1 > max_ {
            max_ = j-i+1
            start = i
        }
    }

    for i:=0;i<len(s);i++ {
        if i > 0 && s[i] == s[i-1] {
            check(i-1, i)
        }
        if i > 0 && i < len(s)-1 && s[i-1] == s[i+1] {
            check(i-1, i+1)
        }
    }
    return s[start:start+max_]
}
