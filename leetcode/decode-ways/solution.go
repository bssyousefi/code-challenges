// First solution (beats 100%) (DP)
func numDecodings(s string) int {
    l := len(s)
    dp := make([]int,l)
    if s[l-1] != '0' {
        dp[l-1]++
    }
    for i:=l-2;i>=0;i-- {
        if s[i] != '0' {
            dp[i] += dp[i+1]
            if s[i] == '1' || (s[i]=='2' && s[i+1]!='9' && s[i+1]!='8' && s[i+1]!='7') {
                if i+2 < l {
                    dp[i] += dp[i+2]
                } else {
                    dp[i]++
                }
            }
        }
    }
    return dp[0]
}
// Second solution (beats 5%) (recursive, top down)
func numDecodings(s string) int {
    l := len(s)
    cache := make([]int, l)
    var cal func(int)int
    cal = func(i int) int {
        if i >= l {
            return 1
        }
        if s[i] == '0' {
            return 0
        }
        if cache[i] > 0 {
            return cache[i]
        }
        ret := cal(i+1)
        if i < l-1 && (s[i] == '1' || (s[i]=='2' && s[i+1]!='9' && s[i+1]!='8' && s[i+1]!='7')) {
            ret += cal(i+2)
        }
        cache[i] = ret
        return ret
    }
    return cal(0)
}
