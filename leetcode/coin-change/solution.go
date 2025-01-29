// First solution (beats 80%) (DP)
func coinChange(coins []int, amount int) int {
    sort.Slice(coins, func(i,j int)bool{return coins[j]<coins[i]})
    dp := make([]int, amount+1)
    q := []int{0}
    for len(q) > 0 {
        v := q[0]
        q = q[1:]
        for _, c := range coins {
            if v+c <= amount && dp[v+c] == 0 {
                dp[v+c] = dp[v] + 1
                if v+c == amount {
                    q = q[len(q):]
                    break
                }
                q = append(q, v+c)
            }
        }
    }
    if amount == 0 {
        return 0
    }
    if dp[amount] == 0 {
        return -1
    } else {
        return dp[amount]
    }
}
// Second solution (beats 92%) (DP) (initilize slice with cap)
func coinChange(coins []int, amount int) int {
    sort.Slice(coins, func(i,j int)bool{return coins[j]<coins[i]})
    dp := make([]int, amount+1)
    q := make([]int,1,1+amount)
    q[0] = 0
    for len(q) > 0 {
        v := q[0]
        q = q[1:]
        for _, c := range coins {
            if v+c <= amount && dp[v+c] == 0 {
                dp[v+c] = dp[v] + 1
                if v+c == amount {
                    q = q[len(q):]
                    break
                }
                q = append(q, v+c)
            }
        }
    }
    if amount == 0 {
        return 0
    }
    if dp[amount] == 0 {
        return -1
    } else {
        return dp[amount]
    }
}
