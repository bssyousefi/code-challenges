// First solutin (beats 90%) (min heap)
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
    l, r := 2*i+1, 2*i+2

    if l < h.l && h.data[min_] > h.data[l] {
        min_ = l
    }

    if r < h.l && h.data[min_] > h.data[r] {
        min_ = r
    }
    if min_ != i {
        h.data[i], h.data[min_] = h.data[min_], h.data[i]
        h.heapify(min_)
    }
}

func findKthLargest(nums []int, k int) int {
    h := &Heap{data: nums[:k], l: k}
    h.heap()
    for i:=k;i<len(nums);i++ {
        if nums[i] > h.data[0] {
            h.data[0] = nums[i]
            h.heapify(0)
        }
    }
    return h.data[0]
}
