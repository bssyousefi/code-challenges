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
