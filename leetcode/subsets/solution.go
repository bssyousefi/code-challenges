// First solution (beats 100%)
func subsets(nums []int) [][]int {
    if len(nums) == 0 {
        return [][]int{[]int{}}
    }

    ret := subsets(nums[:len(nums)-1])
    l := len(ret)
    for i:=0;i<l;i++ {
        o := []int{nums[len(nums)-1]}
        o = append(o, ret[i]...)
        ret = append(ret, o)
    }
    return ret
}
