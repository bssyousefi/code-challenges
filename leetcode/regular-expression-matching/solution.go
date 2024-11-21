func isMatch(s string, p string) bool {
    cache := make(map[[2]int]bool)
    return check(cache, s, p, 0, 0)
}
func check(cache map[[2]int]bool, s string, p string, i int, j int) bool {
    var ret bool
    if ret, ok := cache[[2]int{i,j}]; ok {
        return ret 
    }
    if len(p) == j && len(s) == i {
        cache[[2]int{i,j}] = true
        return true
    }
    if len(p) == j {
        cache[[2]int{i,j}] = false
        return false
    }
    if len(s) == i {
        if len(p) > j+1 && p[j+1] == '*' {
            return check(cache, s, p, i, j+2)
        } else {
            cache[[2]int{i,j}] = false
            return false
        }
    }
    if len(p) > j+1 && p[j+1] == '*' {
        if p[j] == s[i] || p[j] == '.' {
            ret = check(cache, s, p, i, j+2)
            ret = ret || check(cache, s, p, i+1, j)
        } else {
            ret = check(cache, s, p, i, j+2)
        }
    } else {
        if p[j] == s[i] || p[j] == '.' {
            ret = check(cache, s, p, i+1, j+1)
        } else {
            ret = false
        }
    }
    cache[[2]int{i,j}] = ret
    return ret
}
