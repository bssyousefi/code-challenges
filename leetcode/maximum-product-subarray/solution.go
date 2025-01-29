// First solution (beats 100%) (DP)
func maxProduct(nums []int) int {
    l := len(nums)
    dp := make([][3]int, l)
    // overall Max, Max starting here, Min starting here
    dp[l-1] = [3]int{nums[l-1],nums[l-1],nums[l-1]}
    for i:=l-2;i>-1;i-- {
        a := max(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
        c := min(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
        b := max(a, dp[i+1][0])
        dp[i] = [3]int{b, a, c}
    }
    return dp[0][0]
}
// Second solution (beats 100%) (Mathematical solution)
func maxProduct(nums []int) int {
    l := len(nums)
    rev := make([]int, l)
    for i, j := range nums {
        rev[l-i-1] = j
    }
    max_ := max(nums[0], rev[0])
    for i:=1;i<l;i++ {
        if nums[i-1] != 0 {
            nums[i] *= nums[i-1]
        }
        if nums[i] > max_ {
            max_ = nums[i]
        }
        if rev[i-1] != 0 {
            rev[i] *= rev[i-1]
        }
        if rev[i] > max_ {
            max_ = rev[i]
        }
    }
    return max_
}
