// First solution (beats 65%)
func findDuplicate(nums []int) int {
    l := make([]int, len(nums) - 1)
    for _, i := range nums {
        if l[i-1] == 0 {
            l[i-1] = 1
        } else {
            return i
        }
    }
    return -1
}

// Another solution (beats 65%) (fast-slow solution)
func findDuplicate(nums []int) int {
    slow := nums[nums[0]]
    fast := nums[slow]
    for slow != fast{
        fast = nums[nums[fast]]
        slow = nums[slow]
    }
    slow = nums[0]
    for slow != fast {
        slow = nums[slow]
        fast = nums[fast]
    }
    return slow
}
