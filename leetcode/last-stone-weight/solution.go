// First solution (beats 100%) (heap)
type Heap struct {
    data []int
}

func (h *Heap) heapify(n int, i int) {
    max_ := i
    l, r := 2*i+1, 2*i+2

    if l < n && h.data[l] > h.data[max_] {
        max_ = l
    }
    if r < n && h.data[r] > h.data[max_] {
        max_ = r
    }

    if max_ != i {
        h.data[i], h.data[max_] = h.data[max_], h.data[i]
        h.heapify(n, max_)
    }
}

func (h *Heap) makeHeap(n int) {
    for i:=(n-1)/2;i>=0;i-- {
        h.heapify(n, i)
    }
}

func (h *Heap) push(val int) {
    h.data = append(h.data, val)
    h.makeHeap(len(h.data))
}

func (h *Heap) pop() int {
    ret := h.data[0]
    h.data[0], h.data[len(h.data)-1] = h.data[len(h.data)-1], h.data[0]
    h.data = h.data[:len(h.data)-1]
    h.heapify(len(h.data), 0)
    return ret
}

func lastStoneWeight(stones []int) int {
    h := Heap{data: stones}
    h.makeHeap(len(stones))

    for len(h.data) > 1 {
        s1 := h.pop()
        s2 := h.pop()
        if s1 > s2 {
            h.push(s1-s2)
        }
    }
    if len(h.data) == 1 {
        return h.data[0]
    } else {
        return 0
    }
}
