// First solution (beats 64%) (Greedy)
func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i,j int)bool{return intervals[i][1] < intervals[j][1]})
    ret := 0
    end := intervals[0][1]
    for i:=1;i<len(intervals);i++ {
        if intervals[i][0] >= end {
            end = intervals[i][1]
        } else {
            ret++
        }
    }
    return ret
}
