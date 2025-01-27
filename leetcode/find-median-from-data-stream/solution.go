// First solution (Time exceeded) (min max heap)
type Heap struct {
    data []int
    l    int
}

func (h *Heap) heap() {
    for i:=(h.l-1)/2;i>=0;i-- {
        h.heapify(i)
    }
}

func (h *Heap) heapify(i int) {
    min_ := i
    l,r := 2*i+1, 2*i+2

    if l<h.l && h.data[l] < h.data[min_] {
        min_ = l
    }
    if r<h.l && h.data[r] < h.data[min_] {
        min_ = r
    }
    if min_ != i {
        h.data[i], h.data[min_] = h.data[min_], h.data[i]
        h.heapify(min_)
    }
}

func (h *Heap) push(i int) {
    h.data = append(h.data, i)
    h.l++
    h.heap()
}

func (h *Heap) pushpop(i int) int{
    if h.l > 0 && i >= h.data[0] {
        ret := h.data[0]
        h.data[0] = i
        h.heapify(0)
        return ret
    } else {
        return i
    }
}

type MedianFinder struct {
    up   *Heap
    down *Heap
    tmp  int
    isEven bool
}


func Constructor() MedianFinder {
    return MedianFinder {
        up: &Heap{data: make([]int,0,0), l: 0},
        down: &Heap{data: make([]int,0,0), l: 0},
        isEven: true,
    }
}


func (this *MedianFinder) AddNum(num int)  {
    if this.isEven {
        // if this.up.l == 0 {
        //     this.tmp = num
        // } else if this.up.data[0] < num {
        //     this.tmp = this.up.pushpop(num)
        // } else {
        //     this.tmp = -this.down.pushpop(-num)
        // }
        this.up.push(-this.down.pushpop(-num))
        this.isEven = false
    } else {
        // if this.tmp < num {
        //     this.up.push(num)
        //     this.down.push(-this.tmp)
        // } else {
        //     this.down.push(-num)
        //     this.up.push(this.tmp)
        // }
        this.down.push(-this.up.pushpop(num))
        this.isEven = true
    }
}


func (this *MedianFinder) FindMedian() float64 {
    if !this.isEven {
        return float64(this.up.data[0])
    } else {
        return float64(this.up.data[0] - this.down.data[0]) / 2.0
    }
}
// Second solution (beats 6%) (native sort)
type MedianFinder struct {
    data []int
}

func Constructor() MedianFinder {
    return MedianFinder {
        data: []int{},
    }
}

func (this *MedianFinder) AddNum(num int)  {
    this.data = append(this.data, num)
}

func (this *MedianFinder) FindMedian() float64 {
    slices.Sort(this.data)
    l := len(this.data)
    if l%2 == 0 {
        return float64(this.data[l/2-1]+this.data[l/2]) / 2.0
    } else {
        return float64(this.data[l/2])
    }
}


// Third solution (beats 92%) (Optimized version of first solution)
type Heap struct {
    data []int
    l    int
}

func (h *Heap) heap() {
    for i:=(h.l-1)/2;i>=0;i-- {
        h.heapify(i)
    }
}

func (h *Heap) heapify(i int) {
    min_ := i
    l,r := 2*i+1, 2*i+2

    if l<h.l && h.data[l] < h.data[min_] {
        min_ = l
    }
    if r<h.l && h.data[r] < h.data[min_] {
        min_ = r
    }
    if min_ != i {
        h.data[i], h.data[min_] = h.data[min_], h.data[i]
        h.heapify(min_)
    }
}

func (h *Heap) push(i int) {
    h.data = append(h.data, i)
    h.l++
    for j:=h.l-1;j>=0; {
        p := (j-1) / 2
        if h.data[p] > h.data[j] {
            h.data[p], h.data[j] = h.data[j], h.data[p]
            j = p
        } else {
            break
        }
    }
    //h.heap()
}

func (h *Heap) pushpop(i int) int{
    if h.l > 0 && i >= h.data[0] {
        ret := h.data[0]
        h.data[0] = i
        h.heapify(0)
        return ret
    } else {
        return i
    }
}

func (h *Heap) pop() int {
    ret := h.data[0]
    h.data[0], h.data[h.l-1] = h.data[h.l-1], h.data[0]
    h.l--
    h.data = h.data[:h.l]
    h.heapify(0)
    return ret
}

type MedianFinder struct {
    up   *Heap
    down *Heap
    tmp  int
    isEven bool
}


func Constructor() MedianFinder {
    up := make([]int,0,0)
    down := make([]int,0,0)
    return MedianFinder {
        up: &Heap{data: up, l: 0},
        down: &Heap{data: down, l: 0},
        isEven: true,
    }
}


func (this *MedianFinder) AddNum(num int)  {
    if this.isEven {
        // if this.up.l == 0 {
        //     this.tmp = num
        // } else if this.up.data[0] < num {
        //     this.tmp = this.up.pushpop(num)
        // } else {
        //     this.tmp = -this.down.pushpop(-num)
        // }
        // this.up.push(-this.down.pushpop(-num))
        if this.up.l > 0 && this.up.data[0] > num {
            this.down.push(-num)
            this.up.push(-this.down.pop())
        } else {
            this.up.push(num)
        }
        this.isEven = false
    } else {
        // if this.tmp < num {
        //     this.up.push(num)
        //     this.down.push(-this.tmp)
        // } else {
        //     this.down.push(-num)
        //     this.up.push(this.tmp)
        // }
        // this.down.push(-this.up.pushpop(num))
        if this.up.data[0] > num {
            this.down.push(-num)
        } else {
            this.up.push(num)
            this.down.push(-this.up.pop())
        }
        this.isEven = true
    }
}


func (this *MedianFinder) FindMedian() float64 {
    if !this.isEven {
        return float64(this.up.data[0])
    } else {
        return float64(this.up.data[0] - this.down.data[0]) / 2.0
    }
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
