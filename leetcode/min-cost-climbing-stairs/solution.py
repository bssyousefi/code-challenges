# First solution (beats 100%) (DP)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_ = [0] * (len(cost)+1)
        if len(cost) < 2:
            return 0

        for i in range(2, len(min_)):
            min_[i] = min(min_[i-1]+cost[i-1], min_[i-2]+cost[i-2])

        return min_[-1]
