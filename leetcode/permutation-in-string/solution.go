func checkInclusion(s1 string, s2 string) bool {
    m := [26]int{0}
    n := [26]int{0}
    l := 1
    if len(s2) < len(s1) {
        return false
    }
    for i,_ := range s1 {
        m[s1[i] - 'a'] = m[s1[i] - 'a'] + 1
        n[s2[i] - 'a'] = n[s2[i] - 'a'] + 1
    }
    if m == n {
        return true
    }

    for i:=len(s1);i<len(s2);i=i+1 {
        n[s2[l-1]-'a'] = n[s2[l-1]-'a'] - 1
        n[s2[i]-'a'] = n[s2[i]-'a'] + 1

        if m == n {
            return true
        }
        l = l + 1
    }
    return false
}
// New solution (beats 100%)
func checkInclusion(s1 string, s2 string) bool {
    _map := [26]int{0}
    for i:=0; i<len(s1); i++ {
        _map[s1[i] - 'a']++
    }
    i, j := 0, 0
    for j < len(s2){
        if _map[s2[j] - 'a'] > 0 {
            _map[s2[j] - 'a']--
            if j - i + 1 == len(s1) {
                return true
            }
            j++
        } else {
            for _map[s2[j] - 'a'] == 0 && i < j {
                _map[s2[i] - 'a']++
                i++
            }
        }
        if i == j {
            for j < len(s2) && _map[s2[j] - 'a'] == 0 {
                j++
            }
            i = j
        }
    }
    return false
}
