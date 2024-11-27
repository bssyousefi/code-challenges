// First solution (beats 88%)
func threeSum(nums []int) [][]int {
    var i, j, k int
    ret := make([][]int, 0)
    i = 0
    l := len(nums)
    sort.Slice(nums, func(i, j int) bool {return nums[i] < nums[j]})
    for i < l - 2 {
        if nums[i] > 0 {
            break
        }
        if i > 0 && nums[i] == nums[i-1] {
            i += 1
            continue
        }
        k = i + 1
        j = l - 1
        for k < j {
            v := nums[i] + nums[k] + nums[j]
            if v < 0 {
                k += 1
            } else if v > 0 {
                j -= 1
            } else {
                ret = append(ret, []int{nums[i], nums[k], nums[j]})
                k += 1
                j -= 1
                for nums[j] == nums[j+1] && k < j {
                    j -= 1
                }
            }
        }
        i += 1
    }
    return ret
}
