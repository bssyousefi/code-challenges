// First solution (beats 36%) (brute force)
func isNStraightHand(hand []int, groupSize int) bool {
    m := map[int]int{}
    n := []int{}
    l := len(hand)
    if l % groupSize > 0 {
        return false
    }

    for _, i := range hand {
        if _, ok := m[i]; ok {
            m[i]++
        } else {
            m[i] = 1
            n = append(n, i)
        }
    }

    slices.Sort(n)

    for _, i := range n {
        k := m[i]
        if k == 0 {
            continue
        }
        for j := 0; j<groupSize;j++ {
            m[i+j] -= k
            if m[i+j] < 0 {
                return false
            }
        }
    }
    return true
}
// Second solution (beats 68%) (min heap)
type Heap struct {
    data []int
    l    int
}

func (h *Heap) push(i int) {
    h.data = append(h.data, i)
    h.l++
    child := h.l-1
    for child > 0 {
        parent := (child-1) / 2
        if h.data[parent] > h.data[child] {
            h.data[child], h.data[parent] = h.data[parent], h.data[child]
            child = parent
        } else {
            break
        }
    }
}

func (h *Heap) pop() int {
    ret := h.data[0]
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    h.l--
    h.data = h.data[:h.l]
    parent := 0
    for parent < h.l {
        l, r := parent*2+1, parent*2+2
        min_ := parent

        if l < h.l && h.data[l] < h.data[min_] {
            min_ = l
        }
        if r < h.l && h.data[r] < h.data[min_] {
            min_ = r
        }
        if min_ != parent {
            h.data[parent], h.data[min_] = h.data[min_], h.data[parent]
            parent = min_
        } else {
            break
        }
    }
    return ret
}

func isNStraightHand(hand []int, groupSize int) bool {
    m := map[int]int{}
    n := Heap{}
    l := len(hand)
    if l % groupSize > 0 {
        return false
    }

    for _, i := range hand {
        if _, ok := m[i]; ok {
            m[i]++
        } else {
            m[i] = 1
            n.push(i)
        }
    }


    for n.l > 0 {
        i := n.pop()
        k := m[i]
        if k == 0 {
            continue
        }
        for j := 0; j<groupSize;j++ {
            m[i+j] -= k
            if m[i+j] < 0 {
                return false
            }
        }
    }
    return true
}
// Third solution (beats 96%) (without sorting)
func isNStraightHand(hand []int, groupSize int) bool {
    m := map[int]int{}
    l := len(hand)
    if l % groupSize > 0 {
        return false
    }

    for _, i := range hand {
        m[i]++
    }


    for _, i := range hand {
        if m[i] == 0 {
            continue
        }
        start := i
        for m[start-1] > 0 {
            start--
        }
        for start <= i {
            if m[start] > 0 {
                k := m[start]
                for j:=0;j<groupSize;j++ {
                    m[start+j] -= k
                    if m[start+j] < 0 {
                        return false
                    }
                }
            }
            start++
        }
    }
    return true
}
