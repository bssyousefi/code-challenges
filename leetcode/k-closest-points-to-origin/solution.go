// First solution (beats 99%) (built-in sort)
func kClosest(points [][]int, k int) [][]int {
    slices.SortFunc(points, func(i []int, j []int)int{return i[0]*i[0]+i[1]*i[1] - j[0]*j[0]-j[1]*j[1]})
    return points[:k]
}
// Second solution (beats 99%) (max heap)
type Heap struct {
    data [][]int
}
func (h *Heap) heap() {
    for i:=(len(h.data)-1)/2;i>-1;i-- {
        h.heapify(len(h.data), i)
    }
}

func (h *Heap) heapify(n, i int) {
    max_ := i
    l, r := 2*i+1, 2*i+2

    if l < n && getVal(h.data[l]) > getVal(h.data[max_]) {
        max_ = l
    }

    if r < n && getVal(h.data[r]) > getVal(h.data[max_]) {
        max_ = r
    }
    if max_ != i {
        h.data[max_], h.data[i] = h.data[i], h.data[max_]
        h.heapify(n, max_)
    }
}

func getVal(i []int) int {
    return i[0]*i[0]+i[1]*i[1]
}
func kClosest(points [][]int, k int) [][]int {
    h := Heap{data: points[:k]}
    h.heap()
    for i:=k;i<len(points);i++ {
        if getVal(points[i]) < getVal(h.data[0]) {
            h.data[0] = points[i]
            h.heapify(k, 0)
        }
    }
    return h.data
}
