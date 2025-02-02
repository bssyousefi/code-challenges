// First solution (beats 24%) (DP)
func canPartition(nums []int) bool {
    s := 0
    for _, i := range nums {
        s += i
    }
    if s%2==1 {
        return false
    }
    s /= 2
    d := map[int]bool{}
    for _, i := range nums {
        tmp := make([]int,0,len(d))
        for j, _ := range d {
            if (j+i) < s {
                tmp = append(tmp,j+i)
            } else if (j+i) == s {
                return true
            }
        }
        d[i] = true
        for _, j := range tmp {
            d[j] = true
        }
    }
    return d[s]
}
// Second solution (beats 91%) (DP, bottom up)
func canPartition(nums []int) bool {
    s := 0
    for _, i := range nums {
        s += i
    }
    if s%2==1 {
        return false
    }
    s /= 2
    d := make([]bool,s+1)
    d[0] = true
    for _, i := range nums {
        if i > s {
            return false
        }
        for j:=s;j>=i;j-- {
            if !d[j-i] {
                continue
            } else if j == s {
                return true
            } else {
                d[j] = true
            }
        }
    }
    return d[s]
}
