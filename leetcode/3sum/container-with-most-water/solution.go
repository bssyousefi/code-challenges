// First solution (beats 20%)
func maxArea(height []int) int {
    _max := 0
    _len := len(height)
    l := [][2]int{{0, height[0]}}
    r := [][2]int{{_len-1, height[_len-1]}}

    for i:= 1; i < _len; i++ {
        if v:=height[i]; v > l[len(l)-1][1] {
            l = append(l, [2]int{i, v})
        }
        if v:=height[_len-1-i]; v > r[len(r)-1][1] {
            r = append(r, [2]int{_len-1-i, v})
        }
    }
    i, j := 0, 0
    for i < len(l) && j < len(r) && l[i][0] < r[j][0] {
        if l[i][1] < r[j][1] {
            if v:=(l[i][1] * (r[j][0] - l[i][0])); v > _max {
                _max = v
            }
            i += 1
        } else {
            if v:=(r[j][1] * (r[j][0] - l[i][0])); v > _max {
                _max = v
            }
            j += 1
        }
    }
    return _max
}

// Second solution (beats 100%) (obvious solution)
func maxArea(height []int) int {
    _max := 0
    _len := len(height)

    i, j := 0, _len-1
    for i < j {
        if height[i] < height[j] {
            if v:=(height[i] * (j - i)); v > _max {
                _max = v
            }
            i += 1
        } else {
            if v:=(height[j] * (j - i)); v > _max {
                _max = v
            }
            j -= 1
        }
    }
    return _max
}
