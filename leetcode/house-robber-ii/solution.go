// First solution (beats 100%) (DP)
func rob(nums []int) int {
    var cal func(i int, s int) int
    n := len(nums)
    cache := map[[2]int]int{}

    cal = func(i, s int) int {
        if i >= n {
            return 0
        } else if i == 0 {
            return max(cal(2, 1)+nums[0], cal(1, 0))
        } else if i == n-1 {
            if s == 0 {
                return nums[i]
            } else {
                return 0
            }
        } else {
            ok := false
            v := 0
            if v, ok = cache[[2]int{i, s}]; !ok {
                v = max(cal(i+2, s)+nums[i], cal(i+1, s))
                cache[[2]int{i, s}] = v
            }
            return v
        }
    }
    return cal(0, 0)
}
