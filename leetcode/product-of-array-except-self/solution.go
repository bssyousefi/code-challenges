// First solution
func productExceptSelf(nums []int) []int {
    l := len(nums)
    lr := make([]int, l)
    rl := make([]int, l)
    lr[0] = 1
    rl[l-1] = 1
    ret := make([]int, l)

    for i:=1;i<l;i++ {
        lr[i] = lr[i-1] * nums[i-1]
        rl[l-1-i] = rl[l-i] * nums[l-i]
    }
    for i:=0;i<l;i++ {
        ret[i] = lr[i] * rl[i]
    }
    return ret
}

// Second solution (optimized) (beats 100%)
func productExceptSelf(nums []int) []int {
    l := len(nums)
    lr := make([]int, l)
    lr[0] = 1
    var holder int = 1

    for i:=1;i<l;i++ {
        lr[i] = lr[i-1] * nums[i-1]
    }
    for i:=1;i<l;i++ {
        holder *= nums[l-i]
        lr[l-1-i] = lr[l-1-i] * holder
    }
    return lr
}
