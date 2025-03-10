// First solution (beats 97%) (BFS + min heap)
type Heap struct {
    data [][2]int
    l    int
}

func (h *Heap) push(node [2]int) {
    h.data = append(h.data, node)
    h.l++
    cur := h.l-1
    for cur >= 0 {
        p := (cur-1) / 2
        if h.data[p][0] > h.data[cur][0] {
            h.data[p], h.data[cur] = h.data[cur], h.data[p]
            cur = p
        } else {
            break
        }
    }
}

func (h *Heap) pop() [2]int {
    ret := h.data[0]
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    h.l--
    h.data = h.data[:h.l]
    cur := 0
    for cur >= 0 {
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
    return ret
}

func networkDelayTime(times [][]int, n int, k int) int {
    m := map[int][][2]int{}
    for i:=0;i<len(times);i++ {
        m[times[i][0]] = append(m[times[i][0]], [2]int{times[i][1], times[i][2]})
    }

    q := Heap{}
    q.push([2]int{0, k})
    seen := make([]bool, n)
    tmp := make([]int, n)
    ret := 0

    for q.l > 0 {
        node := q.pop()
        if seen[node[1]-1] {
            continue
        }
        seen[node[1]-1] = true
        ret = node[0]
        for _, i:= range m[node[1]] {
            if tmp[i[0]-1] == 0 || tmp[i[0]-1] > (node[0]+i[1]) {
                tmp[i[0]-1] = node[0]+i[1]
                q.push([2]int{i[1]+node[0], i[0]})
            }
        }
    }
    state := true
    for _, i := range seen {
        if i == false {
            state = false
            break
        }
    }
    if state {
        return ret
    } else {
        return -1
    }
}
