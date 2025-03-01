// First solution (beats 100%)
func checkValidString(s string) bool {
    open := 0
    close := 0
    l := len(s)

    for i:=0;i<l;i++ {
        if s[i] == ')' {
            open--
        } else {
            open++
        }

        if s[l-i-1] == '(' {
            close--
        } else {
            close++
        }

        if open < 0 || close < 0 {
            return false
        }
    }
    return true
}
