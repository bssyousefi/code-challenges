// First solution (beats 100%)
func isValid(s string) bool {
    if l:= len(s); l%2 != 0 {
        return false
    } else {
        _stack := make([]byte, l/2)
        _map := map[byte]byte{'(': ')', '[': ']', '{': '}'}
        counter := 0
        for i:=0; i < l; i++ {
            if v, ok := _map[s[i]]; ok {
                if counter >= l/2 {
                    return false
                }
                _stack[counter] = v
                counter++
            } else {
                if counter <= 0 || _stack[counter-1] != s[i] {
                    counter--
                    return false
                }
                counter--
            }
        }
        if counter != 0 {
            return false
        } else {
            return true
        }
    }
}
