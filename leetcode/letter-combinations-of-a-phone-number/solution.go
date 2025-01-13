func letterCombinations(digits string) []string {
    cache := map[byte]string{
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz",
    }
    return cal(digits, cache)
}

func cal(digits string, c map[byte]string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    v := cal(digits[1:], c)
    ret := []string{}
    for _, i := range c[digits[0]] {
        if len(v) == 0 {
            ret = append(ret, string(i))
        } else {
            for _, j := range v {
                ret = append(ret, string(i) + j)
            }
        }
    }
    return ret
}
