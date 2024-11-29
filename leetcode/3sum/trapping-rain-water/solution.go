// First solution (beats 100%) (vertical calculation)
func trap(height []int) int {
    area := 0
    l, r := 0, len(height) - 1
    lmax, rmax := 0, 0

    for l < r {
        if height[l] < height[r] {
            if height[l] > lmax {
                lmax = height[l]
            } else {
                area += lmax - height[l]
            }
            l++
        } else {
            if height[r] > rmax {
                rmax = height[r]
            } else {
                area += rmax - height[r]
            }
            r--
        }
    }
    return area
}
