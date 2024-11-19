func containsDuplicate(nums []int) bool {
    _map := make(map[int]int)
    for i:=0;i<len(nums);i++ {
        if _, ok := _map[nums[i]]; ok {
            return true
        }
        _map[nums[i]] = 0
    }
    return false
}
