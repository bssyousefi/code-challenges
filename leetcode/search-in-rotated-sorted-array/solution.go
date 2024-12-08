func search(nums []int, target int) int {
    l := 0
    r := len(nums) - 1

    for l <= r {
        m := (l+r) / 2
        if nums[m] == target {
            return m
        }
        if nums[l] <= nums[m] {
            if (nums[m] > target && nums[l] > target) || nums[m] < target {
                l = m + 1
            } else {
                r = m - 1
            }
        } else {
            if (nums[m] < target && nums[r] < target) || nums[m] > target {
                r = m - 1
            } else {
                l = m + 1
            }
        }
    }
    return -1
}
// New solution (beats 100%)
func search(nums []int, target int) int {
    i, j := 0, len(nums) - 1
    for i < j {
        m := (i + j) / 2
        if nums[m] == target {
            return m
        } else if nums[m] > target {
            if nums[m] < nums[j] {
                j = m - 1
            } else if nums[i] <= target {
                j = m - 1
            } else {
                i = m + 1
            }
        } else {
            if nums[m] > nums[j] {
                i = m + 1
            } else if nums[j] >= target {
                i = m + 1
            } else {
                j = m - 1
            }
        }
    }
    if nums[i] == target {
        return i
    } else {
        return -1
    }
}
