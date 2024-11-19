func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    _map := make(map[rune]int)
    for _,c := range s {
        _map[c] += 1
    }

    for _,c := range t {
        _map[c] -= 1
        if _map[c] < 0 {
            return false
        }
    }
    return true
}
