// First solution (beats 40%) (DP)
func lengthOfLIS(nums []int) int {
    l := len(nums)
    ret := 1
    dp := make([]int, l)
    for i:=0;i<l;i++ {
        dp[i] = 1
    }

    for i:=l-2;i>=0;i-- {
        for j:=i+1;j<l;j++ {
            if nums[i] < nums[j] && dp[i] < dp[j]+1 {
                dp[i] = dp[j] + 1
                if ret < dp[i] {
                    ret = dp[i]
                }
            }
        }
    }
    return ret
}
// Second solution (beats 100%) (Bissect)
func lengthOfLIS(nums []int) int {
    l := len(nums)
    arr := []int{nums[0]}
    for i:=1;i<l;i++ {
        idx := 0
        for j:=len(arr)-1;j>=0;j-- {
            if arr[j] < nums[i] {
                idx = j + 1
                break
            }
        }
        if idx == len(arr) {
            arr = append(arr, nums[i])
        } else {
            arr[idx] = nums[i]
        }
    }
    return len(arr)
}
