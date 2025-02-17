// First solution (beats 100%) (greedy)
func jump(nums []int) int {
    l := len(nums)
    max_ := 0
    end := 0
    steps := 0

    for i:=0;i<l-1;i++ {
        if v:=i+nums[i]; v > max_ {
            max_ = v
            if v >= l-1 {
                return steps+1
            }
        }
        if i == end {
            steps++
            end = max_
        }
    }
    return steps
}
