// First solution (beats 96%) (min heap)
type Heap struct {
    data [][2]int
    l    int
}

func (h *Heap) push(v [2]int) {
    h.data = append(h.data, v)
    h.l++
    cur := h.l - 1
    for cur > 0 {
        p := (cur - 1) / 2
        if h.data[p][0] > h.data[cur][0] {
            h.data[p], h.data[cur] = h.data[cur], h.data[p]
            cur = p
        } else {
            break
        }
    }
}

func (h *Heap) pop() {
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    h.l--
    h.data = h.data[:h.l]
    cur := 0
    for cur < h.l {
        min_ := cur
        l, r := 2*cur+1, 2*cur+2

        if l < h.l && h.data[l][0] < h.data[min_][0] {
            min_ = l
        }
        if r < h.l && h.data[r][0] < h.data[min_][0] {
            min_ = r
        }

        if min_ != cur {
            h.data[min_], h.data[cur] = h.data[cur], h.data[min_]
            cur = min_
        } else {
            break
        }
    }
}

func minInterval(intervals [][]int, queries []int) []int {
    sort.Slice(intervals, func (i,j int) bool {return intervals[i][0] < intervals[j][0]})
    qCopy := make([]int,len(queries))
    for i, j := range queries {
        qCopy[i] = j
    }
    slices.Sort(qCopy)
    res := map[int]int{}
    h := Heap{data:[][2]int{}, l:0}
    i := 0
    for _, q := range qCopy {
        for i<len(intervals) && intervals[i][0] <= q {
            v := intervals[i]
            h.push([2]int{v[1]-v[0]+1, v[1]})
            i++
        }
        for h.l>0 && h.data[0][1] < q {
            h.pop()
        }
        if h.l> 0 {
            res[q] = h.data[0][0]
        } else {
            res[q] = -1
        }
    }
    for i, _ := range qCopy {
        qCopy[i] = res[queries[i]]
    }
    return qCopy
}
