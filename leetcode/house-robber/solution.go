// First solution )beats 100%) (memoized DFS)
func rob(nums []int) int {
    cache := map[int]int{}
    var dfs func(int) int
    dfs = func(i int) int{
        if i >= len(nums) {
            return 0
        }
        var v int
        var ok bool
        if v, ok = cache[i]; !ok {
            v = max(nums[i]+dfs(i+2), dfs(i+1))
            cache[i] = v
        }
        return v
    }
    return dfs(0)
}
