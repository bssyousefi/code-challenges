// First solution (beats 98%)
func dailyTemperatures(temperatures []int) []int {
    ret := make([]int, len(temperatures))
    stack := []int{0}
    count := 1

    for i:=1; i < len(temperatures); i++ {
        for count > 0 && temperatures[stack[count-1]] < temperatures[i] {
            ret[stack[count-1]] = i - stack[count-1]
            count--
        }
        if count == len(stack) {
            stack = append(stack, i)
            count++
        } else {
            stack[count] = i
            count++
        }
    }
    return ret
}
