// First solution (beats 100%)
func evalRPN(tokens []string) int {
    _stack := []int{}
    count := 0
    for _, token := range tokens {
        switch token {
            case "+":
                _stack[count-2] = _stack[count-1] + _stack[count-2]
                count--
            case "-":
                _stack[count-2] = _stack[count-2] - _stack[count-1]
                count--
            case "*":
                _stack[count-2] = _stack[count-1] * _stack[count-2]
                count--
            case "/":
                _stack[count-2] = _stack[count-2] / _stack[count-1]
                count--
            default:
                v, _ := strconv.Atoi(token)
                if len(_stack) <= count {
                    _stack = append(_stack, v)
                } else {
                    _stack[count] = v
                }
                count++
        }
    }
    return _stack[count-1]
}
