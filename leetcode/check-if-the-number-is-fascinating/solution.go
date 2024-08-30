func isFascinating(n int) bool {
    s := [9]int{}
    var j int
    ns := [3]int{n, 2 * n, 3 * n}
    for _, i := range ns {
        for i > 0 {
            j = i % 10
            if j == 0 {
                return false
            }
            if s[j-1] != 0 {
                return false
            }
            s[j-1] = j 
            i = i / 10
        }
    }
    return true
}
