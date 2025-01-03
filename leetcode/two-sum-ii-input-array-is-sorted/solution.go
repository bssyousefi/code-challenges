// First solution (beats 100%)
func twoSum(numbers []int, target int) []int {
    i, j := 0, len(numbers) - 1

    for i < j {
        if numbers[i] + numbers[j] == target {
            return []int{i+1, j+1}
        } else if numbers[i] + numbers[j] > target {
            j -= 1
        } else {
            i++
        }
    }
    return []int{}
}
