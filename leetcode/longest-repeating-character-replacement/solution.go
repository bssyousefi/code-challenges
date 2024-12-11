// Previous solution (beats 39%)
func characterReplacement(s string, k int) int {
    cache := make(map[byte]int)
    l := 0
    m := 0

    for i:=0; i<len(s); i++ {
        n := cache[s[i]]
        cache[s[i]] = n+1

        if m < n+1 {
            m = n+1
        }

        if i-l+1-m > k {
            cache[s[l]] = cache[s[l]] - 1
            l = l + 1
        }
    }
    return len(s)-l
}
// Second solution (beats 75%) (replace map with slice)
func characterReplacement(s string, k int) int {
    i := 0
    l := len(s)
    _max := 0
    _map := make([]int, 26)

    for j:=0;j<l;j++ {
        _map[s[j] - 'A']++
        if _map[s[j] - 'A'] > _max {
            _max = _map[s[j] - 'A']
        }
        if j-i+1-_max > k {
            _map[s[i] - 'A']--
            i++
        }
    }
    return l - i
}
