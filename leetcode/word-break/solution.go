// First solution (beats 100%) (DP)
func wordBreak(s string, wordDict []string) bool {
    l := len(s)
    dp := make([]bool,l+1)
    dp[l] = true
    words := map[string]bool{}
    for _, v := range wordDict {
        words[v] = true
    }

    for i:=l-1;i>=0;i-- {
        if words[s[i:]] {
            dp[i] = true
            continue
        }
        for j:=i+1;j<l;j++ {
            if dp[j] {
                if words[s[i:j]] {
                    dp[i] = true
                    break
                }
            }
        }
    }
    return dp[0]
}
// Second solution (beats 100%) (DFS) (more memory usage)
func wordBreak(s string, wordDict []string) bool {
    l := len(s)
    cache := map[int]bool{}
    words := map[string]bool{}
    for _, v := range wordDict {
        words[v] = true
    }

    var dfs func(int) bool
    dfs = func(i int) bool {
        if i == l {
            return true
        }
        if v, ok := cache[i]; ok {
            return v
        }
        for j:=i+1;j<=l;j++ {
            if words[s[i:j]] {
                if dfs(j) {
                    cache[i] = true
                    return true
                }
            }
        }
        cache[i] = false
        return false
    }
    return dfs(0)
}
