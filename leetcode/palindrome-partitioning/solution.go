// First solution (beats 29%)
func partition(s string) [][]string {
    cache := make(map[string][][]string)
    return getPartitions(s, &cache)
}

func getPartitions(s string, c *map[string][][]string) [][]string {
    if len(s) == 0 {
        return [][]string{[]string{}}
    }
    ret := [][]string{}
    for i := range s {
        if isPalindrome(s[0:i+1]) {
            if _, ok := (*c)[s[i+1:]]; !ok {
                (*c)[s[i+1:]] = getPartitions(s[i+1:], c)
            }
            v := (*c)[s[i+1:]]
            for _, k := range v {
                tmp := []string{s[:i+1]}
                ret = append(ret, append(tmp, k...))
            }
        }
    }
    return ret
}

func isPalindrome(s string) bool {
    i, j := 0, len(s) - 1
    for i < j {
        if s[i] == s[j] {
            i++
            j--
        } else {
            return false
        }
    }
    return true
}

// Second solution (beats 92%) (initialize slice with proper size)
func partition(s string) [][]string {
    cache := make(map[string][][]string)
    return getPartitions(s, cache)
}

func getPartitions(s string, c map[string][][]string) [][]string {
    if len(s) == 0 {
        return [][]string{[]string{}}
    }
    ret := [][]string{}
    for i := range s {
        if isPalindrome(s[0:i+1]) {
            if _, ok := c[s[i+1:]]; !ok {
                c[s[i+1:]] = getPartitions(s[i+1:], c)
            }
            v := c[s[i+1:]]
            // v := getPartitions(s[i+1:], c)
            for _, k := range v {
                tmp := make([]string, 1, len(k)+1)
                tmp[0] = s[:i+1]
                ret = append(ret, append(tmp, k...))
            }
        }
    }
    return ret
}

func isPalindrome(s string) bool {
    i, j := 0, len(s) - 1
    for i < j {
        if s[i] == s[j] {
            i++
            j--
        } else {
            return false
        }
    }
    return true
}
