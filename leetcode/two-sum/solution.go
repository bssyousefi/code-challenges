func twoSum(nums []int, target int) []int {
    _map := make(map[int]int)
    for i, v := range nums {
        if j, ok := _map[v]; ok {
            return []int{j, i}
        }
        _map[target - v] = i
    }
    return []int{}
}
