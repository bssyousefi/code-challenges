// DP solution (beats 100%)
func combinationSum(candidates []int, target int) [][]int {
    dp := make([][][]int, target)
    for i := range dp {
        dp[i] = [][]int{}
    }
    for _, i := range candidates {
        if i > target {
            continue
        }
        dp[i-1] = append(dp[i-1], []int{i})

        for j:=i;j<target;j++ {
            for _, k := range dp[j-i] {
                v := []int{i}
                v = append(v, k...)
                dp[j] = append(dp[j], v)
            }
        }
    }
    return dp[target-1]
}
