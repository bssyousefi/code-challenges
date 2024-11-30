// First solution (beats 11%)
type MinStack struct {
    stack []int
    min [][2]int
    count int
    minCount int
}

func Constructor() MinStack {
    return MinStack {
        []int{},
        [][2]int{},
        0,
        0,
    }
}

func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
    if this.minCount == 0 || this.min[this.minCount-1][1] > val {
        this.min = append(this.min, [2]int{this.count, val})
        this.minCount++
    }
    fmt.Println(this.minCount)
    this.count++
}

func (this *MinStack) Pop()  {
    if this.count - 1 == this.min[this.minCount-1][0] {
        this.minCount--
        this.min = this.min[:this.minCount]
    }
    this.count--
    this.stack = this.stack[:this.count]
}

func (this *MinStack) Top() int {
    return this.stack[this.count-1]
}

func (this *MinStack) GetMin() int {
    fmt.Println(this.min)
    return this.min[this.minCount-1][1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

// Second solution (beats 89%) (ONLY REMOVE PRINT lines)
type MinStack struct {
    stack []int
    min [][2]int
    count int
    minCount int
}

func Constructor() MinStack {
    return MinStack {
        []int{},
        [][2]int{},
        0,
        0,
    }
}

func (this *MinStack) Push(val int)  {
    this.stack = append(this.stack, val)
    if this.minCount == 0 || this.min[this.minCount-1][1] > val {
        this.min = append(this.min, [2]int{this.count, val})
        this.minCount++
    }
    this.count++
}

func (this *MinStack) Pop()  {
    if this.count - 1 == this.min[this.minCount-1][0] {
        this.minCount--
        this.min = this.min[:this.minCount]
    }
    this.count--
    this.stack = this.stack[:this.count]
}

func (this *MinStack) Top() int {
    return this.stack[this.count-1]
}

func (this *MinStack) GetMin() int {
    return this.min[this.minCount-1][1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
