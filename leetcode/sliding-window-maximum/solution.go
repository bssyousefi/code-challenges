// First solution (beats 94%) (better queue implementation)
func maxSlidingWindow(nums []int, k int) []int {
    ret := make([]int, 0, len(nums)-k+1)
    maxs := make([]int, 0)
    l,r := 0, 0

    for r < len(nums) {
        for (len(maxs)>0) && (nums[maxs[len(maxs)-1]]<nums[r]) {
            maxs = maxs[:len(maxs)-1]
        }
        maxs = append(maxs, r)
        if l > maxs[0] {
            maxs = maxs[1:]
        }
        if r >= k - 1 {
            ret = append(ret, nums[maxs[0]])
            l++
        }
        r++
    }
    return ret
}
// Second solution (beats 60%)
func maxSlidingWindow(nums []int, k int) []int {
    l,r := 0, 0
    maxs := []int{}
    count := 0
    res := []int{}
    for r < len(nums) {
        for count > 0 && nums[r] > nums[maxs[count-1]] {
            count--
        }
        if count >= len(maxs) {
            maxs = append(maxs, r)
        } else {
            maxs[count] = r
        }
        count++

        if l > maxs[0] {
            maxs = maxs[1:]
            count--
        }
        if r-l+1 == k {
            l++
            res = append(res, nums[maxs[0]])
        }
        r++
    }
    return res
}
