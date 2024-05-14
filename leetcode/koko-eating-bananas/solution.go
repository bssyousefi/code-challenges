func minEatingSpeed(piles []int, h int) int {
    min_ := 1
    max_ := 0
    for _, v := range piles {
        if max_ < v {
            max_ = v
        }
    }

    for min_ < max_ {
        m := (min_ + max_) / 2
        n := getMoves(piles, m)

        if n <= h {
            max_ = m
        } else {
            min_ = m + 1
        }
    }
    return min_
}

func getMoves(piles []int, k int) int {
    n := 0
    for _, v := range piles {
        n += v/k
        if v%k != 0 {
            n += 1
        }
    }
    return n
}
