package main

import (
    "flag"
    "fmt"
    "os"
    "strconv"
    "strings"
    "runtime/pprof"
)

var cpuprofile = flag.String("cpuprofile", "", "write cpu profile to file")


type Heap struct {
    data []int
    l    int
}

func (h *Heap) heap() {
    for i:=(h.l-1)/2;i>=0;i-- {
        h.heapify(i, h.l)
    }
}

func (h *Heap) heapify(i int, n int) {
    min_ := i
    min_v := h.data[min_]
    l := 2*i+1
    r := l + 1

    if l<n && h.data[l] < min_v {
        min_ = l
        min_v = h.data[l]
    }
    if r<n && h.data[r] < min_v {
        min_ = r
    }
    if min_ != i {
        h.data[i], h.data[min_] = h.data[min_], h.data[i]
        h.heapify(min_, n)
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
        h.heapify(0, h.l)
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
    h.heapify(0, h.l)
    return ret
}

type MedianFinder struct {
    up   *Heap
    down *Heap
    tmp  int
    isEven bool
}


func Constructor() MedianFinder {
    up := make([]int,0,30000)
    down := make([]int,0,30000)
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

func main() {
    fmt.Println("hello")
    f, _ := os.ReadFile("inputs.txt")
    l := string(f)
    l = l[1:len(l)-1]
    l = strings.ReplaceAll(l," ", "")
    l = strings.ReplaceAll(l,"\"", "")
    commands := strings.Split(l, ",")
    commands = commands[1:]
    f, _ = os.ReadFile("values.txt")
    l = string(f)
    l = l[1:len(l)-1]
    l = strings.ReplaceAll(l," ", "")
    l = strings.ReplaceAll(l,"\"", "")
    l = strings.ReplaceAll(l,"[", "")
    l = strings.ReplaceAll(l,"]", "")
    values := strings.Split(l, ",")
    values = values[1:]
    inputs := make([]int, len(values))

    for i:=0;i<len(values);i++ {
        tmp, _ := strconv.Atoi(values[i])
        inputs[i] = tmp
    }

    m := Constructor()
    n := len(commands)
    fmt.Println(n)
    flag.Parse()
    if *cpuprofile != "" {
        f, _ := os.Create(*cpuprofile)
        pprof.StartCPUProfile(f)
        defer pprof.StopCPUProfile()
    }
    for i:=0;i<n;i++ {
        if commands[i] == "addNum" {
            m.AddNum(inputs[i])
        } else {
            m.FindMedian()
        }
    }
}
