// First solution (beats 100%)
func permute(nums []int) [][]int {
    return cal(nums, make([]bool, len(nums)))
}

func cal(nums []int, visit []bool) [][]int {
    ret := [][]int{}
    for i:=0; i< len(nums); i++ {
        if !visit[i] {
            visit[i] = true
            v := cal(nums, visit)
            for _, k := range v {
                l := []int{nums[i]}
                l = append(l, k...)
                ret = append(ret, l)
            }
            visit[i] = false
        }
    }
    if len(ret) == 0 {
        return [][]int{[]int{}}
    }
    return ret
}
