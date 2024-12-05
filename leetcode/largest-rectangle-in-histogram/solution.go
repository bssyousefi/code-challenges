// First solution (beats 57%)
func largestRectangleArea(heights []int) int {
    heights = append(heights, 0)
    stack := []int{len(heights)-1}
    count := 0
    area := 0

    for i:=0; i<len(heights); i++ {
        for heights[i] < heights[stack[count]] {
            if count == 1 {
                area = max(area, heights[stack[1]] * (i))
            } else {
                area = max(area, heights[stack[count]] * (i - 1 -stack[count-1]))
            }
            count--
        }
        count++
        if count == len(stack) {
            stack = append(stack, i)
        } else {
            stack[count] = i
        }
    }
    return area
}
