// First solution (beats 39%) (DP)
func countSubstrings(s string) int {
    l := len(s)
    dp := make([][]bool,0,l)
    for i:=0;i<l;i++ {
        dp = append(dp, make([]bool,l))
    }
    ret := 0
    for i:=l-1;i>=0;i-- {
        for j:=i;j<l;j++ {
            if s[i] == s[j] && (j-i<2 || dp[i+1][j-1]) {
                ret += 1
                dp[i][j] = true
            }
        }
    }
    return ret
}
// Second solution (beats 100%) (Two pointers)
func countSubstrings(s string) int {
    l := len(s)
    ret := 0

    var check func (i,j int)
    check = func(i, j int) {
        for i>= 0 && j < l && s[i] == s[j] {
            ret++
            i--
            j++
        }
    }

    for i:=0;i<l;i++ {
        check(i,i)
        if i<l-1 && s[i] == s[i+1] {
            check(i,i+1)
        }
    }
    return ret
}
