// (beats 100%)
func searchMatrix(matrix [][]int, target int) bool {
    l := 0
    r := len(matrix) - 1

    for l<=r {
        m := (l+r) / 2
        if matrix[m][0] == target {
            return true
        } else if matrix[m][0] < target {
            l = m + 1
        } else {
            r = m - 1
        }
    }
    if l == 0 {
        return false
    }
    ll := 0
    rr := len(matrix[l-1]) - 1

    for ll<=rr {
        m := (ll+rr) / 2
        if matrix[l-1][m] == target {
            return true
        } else if matrix[l-1][m] < target {
            ll = m + 1
        } else {
            rr = m - 1
        }
    }
    return false
}
