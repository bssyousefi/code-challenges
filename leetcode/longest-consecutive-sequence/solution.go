func longestConsecutive(nums []int) int {
    _map := make(map[int]bool)
    for _,i := range nums {
        _map[i] = true
    }
    _max := 0
    var cur int
    for _, i := range nums {
        if _,ok := _map[i-1]; !ok {
            cur = 0
            _,ok := _map[i]
            for ;ok; i++ {
                cur += 1
                ok = _map[i+1]

            }
            if _max < cur {
                _max = cur
            }
            if _max > (len(nums)/2) {
                return _max
            }
        }
    }
    return _max
}
