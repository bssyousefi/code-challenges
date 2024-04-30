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
