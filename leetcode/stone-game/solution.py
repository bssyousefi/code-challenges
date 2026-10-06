# First solution (beats 28%) (2D bottom up DP)
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)

        dp = [[0]*n for _ in range(n)]

        for l in range(n-1,-1,-1):
            for r in range(l,n):
                left, right = 0, 0
                if (r-l)%2==0:
                    left, right = piles[l], piles[r]
                if l == r:
                    dp[l][r] = left
                else:
                    dp[l][r] = max(left+dp[l+1][r], right+dp[l][r-1])

        return dp[0][n-1] >= (sum(piles)//2+1)

# Second solution (beats 100%) (mathematical proof)
# since piles are even, Alice can take all even indexed piles or all odd indexed piles, and one of them is guaranteed to be larger than the other, so Alice can always win.
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return True
