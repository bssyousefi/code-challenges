// First solution (beats 77%) (max heap)
type Heap struct {
    data []int
    l    int
}

func (h *Heap) heap() {
    for i:=(h.l/2)-1;i>-1;i-- {
        h.heapify(i)
    }
}

func (h *Heap) heapify(i int) {
    max_ := i
    l, r := 2*i+1, 2*i+2

    if l < h.l && h.data[l] > h.data[max_] {
        max_ = l
    }
    if r < h.l && h.data[r] > h.data[max_] {
        max_ = r
    }
    if max_ != i {
        h.data[i], h.data[max_] = h.data[max_], h.data[i]
        h.heapify(max_)
    }
}

func (h *Heap) pop() int {
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    ret := h.data[h.l-1]
    h.l--
    h.data = h.data[:h.l]
    h.heapify(0)
    return ret
}

func (h *Heap) push(i int) {
    h.data = append(h.data, i)
    h.l++
    h.heap()
}


func leastInterval(tasks []byte, n int) int {
    c := [26]int{}
    count := 0
    for _, i := range tasks {
        c[i-'A']++
        if c[i-'A'] == 1 {
            count++
        }
    }
    d := make([]int, 0, count)
    for _, i := range c {
        if i > 0 {
            d = append(d, i)
        }
    }
    h := Heap{data: d, l: count}
    h.heap()
    q := [][2]int{}
    times := 0

    for h.l > 0 || len(q) > 0 {
        if h.l > 0 {
            i := h.pop()
            if i > 1 {
                q = append(q, [2]int{i-1, times})
            }
        }
        if len(q) > 0 && q[0][1] == (times - n) {
            h.push(q[0][0])
            q = q[1:]
        }
        times++
    }
    return times
}
// Second solution (beats 100%) (mathematical solution)
func leastInterval(tasks []byte, n int) int {
    c := [26]int{}
    max_ := 0
    max_count := 0
    for _, i := range tasks {
        c[i-'A']++
        if c[i-'A'] > max_ {
            max_ = c[i-'A']
            max_count = 1
        } else if c[i-'A'] == max_ {
            max_count++
        }
    }

    return max((max_-1)*(n+1)+max_count, len(tasks))
}
