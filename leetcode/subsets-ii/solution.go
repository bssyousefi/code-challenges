// First solution (beats 100%)
func subsetsWithDup(nums []int) [][]int {
    slices.Sort(nums)
    return cal(nums)
}

func cal(nums []int) [][]int {
    res := [][]int{[]int{}}
    if len(nums) == 0 {
        return res
    }
    res = append(res, []int{nums[0]})
    i := 0
    for i+1 < len(nums) && nums[i+1] == nums[i] {
        v := []int{nums[0]}
        v = append(v, res[len(res)-1]...)
        res = append(res, v)
        i++
    }
    ret := [][]int{}
    for _, v := range cal(nums[i+1:]) {
        for _, j := range res {
            tmp := []int{}
            ret = append(ret, append(append(tmp, j...), v...))
        }
    }
    return ret
}
