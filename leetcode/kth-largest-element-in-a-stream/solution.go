// First solution (beats 20%)
type KthLargest struct {
    data []int
    full bool
    len  int
    size int
}


func Constructor(k int, nums []int) KthLargest {
    slices.Sort(nums)
    l := len(nums)
    d := KthLargest{data: make([]int, 0), size: k}
    for i := range(k) {
        if i < l {
            d.data = append(d.data, nums[l-1-i])
            d.len++
        }
    }
    if l >= k {
        d.full = true
    }
    return d
}


func (this *KthLargest) Add(val int) int {
    if this.len == this.size {
        if val <= this.data[this.len-1] {
            return this.data[this.len-1]
        } else {
            i, j := 0, this.len-1
            for i < j {
                m := (i+j) / 2
                if this.data[m] < val {
                    j = m
                } else {
                    i = m+1
                }
            }
            for k:=this.len-1;k>i;k-- {
                this.data[k] = this.data[k-1]
            }
            this.data[i] = val
            return this.data[this.len-1]
        }
    } else {
        if this.len == 0 || val <= this.data[this.len-1] {
            this.data = append(this.data, val)
            this.len++
            return val
        } else {
            i, j := 0, this.len-1
            for i < j {
                m := (i+j) / 2
                if this.data[m] < val {
                    j = m
                } else {
                    i = m+1
                }
            }
            this.data = append(this.data, 5)
            this.len++
            for k:=this.len-1;k>i;k-- {
                this.data[k] = this.data[k-1]
            }
            this.data[i] = val
            return this.data[this.len-1]
        }
    }
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */

// Second solution (beats 92%) (using heap)
type Heap struct {
    data []int
}

func NewHeap(nums []int) Heap{
    h := Heap{data: nums}
    l := len(nums)
    for i:=l/2-1;i>=0;i-- {
        h.Heapify(l, i)
    }
    return h
}

func (h *Heap) Heapify(n int, i int) {
    _min := i
    l, r := i * 2 + 1, i * 2 + 2
    if l < n && h.data[_min] > h.data[l] {
        _min = l
    }
    if r < n && h.data[_min] > h.data[r] {
        _min = r
    }
    if _min != i {
        h.data[i], h.data[_min] = h.data[_min], h.data[i]
        h.Heapify(n, _min)
    }
}

func (h *Heap) Push(val int) {
    h.data = append(h.data, val)
    n := len(h.data)
    i := (n-1) / 2
    for i >= 0 {
        h.Heapify(n, i)
        if i == 0 {
            break
        }
        i = (i-1) / 2
    }
}

func (h *Heap) PushPop(val int) int {
    if val <= h.data[0] {
        return val
    }
    ret := h.data[0]
    h.Push(val)
    h.data[0], h.data[len(h.data)-1] = h.data[len(h.data)-1], h.data[0]
    h.data = h.data[:len(h.data)-1]
    h.Heapify(len(h.data), 0)
    return ret
}

type KthLargest struct {
    data *Heap
    len  int
    size int
}


func Constructor(k int, nums []int) KthLargest {
    slices.Sort(nums)
    l := len(nums)
    d := KthLargest{size: k}
    n := NewHeap(nums[max(0, l-k):])
    d.data = &n
    d.len = min(l, k)
    return d
}


func (this *KthLargest) Add(val int) int {
    if this.len == this.size {
        if val > this.data.data[0] {
            this.data.PushPop(val)
        }
    } else {
        this.data.Push(val)
        this.len++
    }
    return this.data.data[0]
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */
