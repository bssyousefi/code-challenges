// First solution (beats 100%)
func mergeTriplets(triplets [][]int, target []int) bool {
    ret := [3]bool{}
    count := 0
    for _, t := range triplets {
        if t[0] > target[0] || t[1] > target[1] || t[2] > target[2] {
            continue
        }
        for i:=0;i<3;i++ {
            if t[i] == target[i] && !ret[i] {
                ret[i] = true
                count++
                if count == 3 {
                    return true
                }
            }
        }
    }
    return false
}
