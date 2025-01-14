// First solution (beats 100%) (DP, Fibonacci)
func climbStairs(n int) int {
    if n == 1 || n == 2 {
        return n
    }
    p1, p2 := 2, 1
    for i:=3;i<=n;i++ {
        p1, p2 = p1+p2, p1
    }
    return p1
}
