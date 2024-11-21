func groupAnagrams(strs []string) [][]string {
    _maps := make(map[[26]int][]string)
    for _, word := range strs {
        m := parse(word)
        if v, ok := _maps[m]; ok {
            _maps[m] = append(v, word)
        } else {
            _maps[m] = []string{word,}
        }
    }
    ret := make([][]string, 0)
    for _, v := range _maps {
        ret = append(ret, v)
    }

    return ret
}

func parse(word string) [26]int {
    _list := [26]int{0}
    for _, v := range word {
        _list[v-'a'] += 1
    }
    return _list
}
