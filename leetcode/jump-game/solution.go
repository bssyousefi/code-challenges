// First solution (beats 100%) (greedy)
func canJump(nums []int) bool {
    l := len(nums)
    if l <= 1 {
        return true
    }
    for i:=0;i<l-1;i++ {
        if nums[i] <= 0 {
            j := i - 1
            for j >= 0 && nums[j] <= (i-j) {
                j--
            }
            if j == -1 {
                return false
            }
        }
    }
    return true
}
