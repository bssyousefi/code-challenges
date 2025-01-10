// First solution (beats 100%)
func combinationSum2(candidates []int, target int) [][]int {
    slices.Sort(candidates)
    return cal(candidates, target)
}

func cal(candidates []int, target int) [][]int {
    ret := [][]int{}
    i := 0
    for i < len(candidates) {
        v := candidates[i]
        if v > target {
            break
        } else if v == target {
            ret = append(ret, []int{v})
        } else {
            k := cal(candidates[i+1:], target - v)
            for _, j := range k {
                l := []int{v}
                l = append(l, j...)
                ret = append(ret, l)
            }
        }
        for i+1 < len(candidates) && candidates[i+1] == candidates[i] {
            i++
        }
        i++
    }
    return ret
}
