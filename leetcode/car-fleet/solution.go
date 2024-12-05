// Two cars cannot be at the same position initially
// First solution (beats 5%)
func carFleet(target int, position []int, speed []int) int {
    c := make([]Car, len(speed))
    count := 1

    for i, v := range position {
        c[i] = Car{position[i], float64(target - v) / float64(speed[i])}
    }
    sort.SliceStable(c, func(i, j int) bool {return c[i].Pos > c[j].Pos})
    _min := c[0].Time
    for i:=1; i<len(c); i++ {
        if c[i].Pos == c[i-1].Pos {
            continue
        } else if c[i].Time > _min {
            _min = c[i].Time
            count++
        } else {
            _min = max(_min, c[i].Time)
        }
    }
    return count
}

    type Car struct {
        Pos int
        Time    float64
    }
// Second solution (beats 99%) (use other sort func)
func carFleet(target int, position []int, speed []int) int {
    c := make([]Car, len(speed))
    count := 1

    for i, v := range position {
        c[i] = Car{position[i], float64(target - v) / float64(speed[i])}
    }
    //sort.SliceStable(c, func(i, j int) bool {return c[i].Pos > c[j].Pos})
    slices.SortFunc(c, func(a, b Car) int {
		return b.Pos - a.Pos
	})
    _min := c[0].Time
    for i:=1; i<len(c); i++ {
        if c[i].Pos == c[i-1].Pos {
            continue
        } else if c[i].Time > _min {
            _min = c[i].Time
            count++
        } else {
            _min = max(_min, c[i].Time)
        }
    }
    return count
}

    type Car struct {
        Pos int
        Time    float64
    }
