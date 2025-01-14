// First solution (beats 100%)
func minCostClimbingStairs(cost []int) int {
    if len(cost) < 2 {
        return 0
    }
    min_ := make([]int, len(cost)+1)
    for i:=2;i<len(min_);i++ {
        min_[i] = min(min_[i-1]+cost[i-1], min_[i-2]+cost[i-2])
    }
    return min_[len(min_)-1]
}
