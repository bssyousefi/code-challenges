// Previous solution (beats 100%)
func lengthOfLongestSubstring(s string) int {
    cache := make(map[rune]int);
    m := 0
    j := 0
    for i, v := range s {
        tmp, ok := cache[v]
        if ok && (tmp >= j) {
            m = max(m, i-j);
            j = tmp + 1;
        }
        cache[v] = i;
    }
    if m > 0 {
        return max(m, len(s) - j)
    } else {
        return len(s)
    }
}
// solution (beats 81%)
func lengthOfLongestSubstring(s string) int {
    _max := 0
    _min_index := 0
    cache := map[byte]int{}
    for i := range s {
        if j, ok := cache[s[i]]; ok && j >= _min_index {
            if i - _min_index > _max {
                _max = i - _min_index
            }
            _min_index = j + 1
        }
        cache[s[i]] = i
    }
    if len(s) - _min_index > _max {
        return len(s) - _min_index
    } else {
        return _max
    }
}
