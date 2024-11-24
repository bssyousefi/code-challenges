// First solution (beats 100%)
func isPalindrome(s string) bool {
    t := strings.ToLower(s)
    i, j := 0, len(s)-1
    for i < j {
        for i < len(s) && !isAlphaNumeric(t[i]) {
            i += 1
        }
        for j >= 0 && !isAlphaNumeric(t[j]) {
            j -= 1
        }
        if i < j && t[i] != t[j] {
            return false
        }
        i += 1
        j -= 1
    }
    return true
}

func isAlphaNumeric(s byte) bool {
    if (s >= 65 && s <= 90) || (s >= 97 && s <= 122) || (s >= 48 && s <= 57) {
        return true
    }
    return false
}
