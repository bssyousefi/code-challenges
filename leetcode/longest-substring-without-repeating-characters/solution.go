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
