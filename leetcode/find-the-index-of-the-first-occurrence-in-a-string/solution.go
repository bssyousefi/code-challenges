func strStr(haystack string, needle string) int {
    l := len(needle)
    h := len(haystack)
    if (l > h) {
        return -1
    }
    i := 0
    c := 0
    for (i <= h-l) {
        for (needle[c] == haystack[i+c]) {
            c++
            if (c == l) {
                return i
            }
        }
        c = 0
        i++
    }
    return -1
}
