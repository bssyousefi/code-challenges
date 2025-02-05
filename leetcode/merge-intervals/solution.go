// First solution (beats 100%) (built-in sort)
func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func (i,j int)bool {return intervals[i][0]<intervals[j][0]})
    ret := [][]int{}
    i := 0
    for i < len(intervals) {
        l, r := intervals[i][0], intervals[i][1]
        for i < (len(intervals)-1) && intervals[i+1][0] <= r {
            if intervals[i+1][1] > r {
                r = intervals[i+1][1]
            }
            i++
        }
        ret = append(ret, []int{l, r})
        i++
    }
    return ret
}
