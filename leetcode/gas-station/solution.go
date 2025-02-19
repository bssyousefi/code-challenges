// First solution (beats 100%) (logical)
func canCompleteCircuit(gas []int, cost []int) int {
    b := 0
    c := -1
    x := 0

    for i:=0;i<len(gas);i++ {
        tmp := gas[i] - cost[i]
        if c >= 0 {
            c += tmp
        }
        if c < 0 {
            x = -1
        }
        if x == -1 && gas[i] >= cost[i] {
            x = i
            c = tmp
        }
        b += tmp
    }
    if b >= 0 {
        return x
    } else {
        return -1
    }
}
