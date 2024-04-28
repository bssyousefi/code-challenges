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
