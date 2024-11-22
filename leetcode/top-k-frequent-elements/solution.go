func topKFrequent(nums []int, k int) []int {
    _map := make(map[int]int)
    for _, v := range nums {
        if n, ok := _map[v]; ok {
            _map[v] = n + 1
        } else {
            _map[v] = 1
        }
    }
    var keys []int
    for i := range _map {
        keys = append(keys, i)
    }
    sort.Slice(keys, func(i, j int) bool {return _map[keys[i]] > _map[keys[j]]})
    var ret []int
    for i:=0; i<k;i++ {
        ret = append(ret, keys[i])
    }
    return ret
}
