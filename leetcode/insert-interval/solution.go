// First solution (beats 100%) (binary search)
func insert(intervals [][]int, newInterval []int) [][]int {
    l, r := 0, len(intervals) - 1
    for l <= r {
        m := (l+r) / 2
        if intervals[m][1] < newInterval[0] {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    r = l
    for r < len(intervals) && intervals[r][0] <= newInterval[1] {
        r++
    }
    ret := make([][]int,0, len(intervals)+1)
    ret = append(ret, intervals[:l]...)
    if r == l {
        ret = append(ret, newInterval)
    } else {
        ret = append(ret, []int{min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[r-1][1])})
    }
    ret = append(ret, intervals[r:]...)
    return ret
}
