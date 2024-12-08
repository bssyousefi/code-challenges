func findMin(nums []int) int {
    l := 0
    r := len(nums) - 1

    for l < r {
        m := (l+r) / 2
        if nums[l] < nums[r] {
            return nums[l]
        }
        if nums[l] <= nums[m] {
            l = m + 1
        } else {
            r = m
        }
    }
    return nums[r]
}
// beats 100%
func findMin(nums []int) int {
    i, j := 0, len(nums) - 1
    if nums[i] < nums[j] {
        return nums[i]
    }
    for i < j {
        m := (i + j) / 2
        if nums[m] < nums[j] {
            j = m
        } else {
            i = m + 1
        }
    }
    return nums[i]
}
