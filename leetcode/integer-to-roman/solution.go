func intToRoman(num int) string {
    m := map[int][2]string{
        1: {"I", "V"},
        2: {"X", "L"},
        3: {"C", "D"},
        4: {"M", ""},
    }
    counter := 0
    ret := ""
    for num > 0 {
        counter += 1
        i := num % 10
        num = num / 10
        if i < 4 {
            for i > 0 {
                ret = m[counter][0] + ret
                i -= 1
            }
        } else if i == 4 {
            ret = m[counter][0] + m[counter][1] + ret
        } else if i == 5 {
            ret = m[counter][1] + ret
        } else if i < 9 {
            for i > 5 {
                ret = m[counter][0] + ret
                i -= 1
            }
            ret = m[counter][1] + ret
        } else if i == 9 {
            ret = m[counter][0] + m[counter+1][0] + ret
        }
    }
    return ret
}
