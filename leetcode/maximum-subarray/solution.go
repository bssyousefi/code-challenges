// First solution (beats 100%) (greedy)
func maxSubArray(nums []int) int {
    max_ := nums[0]
    cur := nums[0]

    for i:=1;i<len(nums);i++ {
        if cur > 0 {
            cur += nums[i]
        } else {
            cur = nums[i]
        }
        if cur > max_ {
            max_ = cur
        }
    }
    return max_
}
