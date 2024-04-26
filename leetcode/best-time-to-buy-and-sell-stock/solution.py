class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 1e7
        max_ = 0
        for i in range(len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
                continue
            max_ = max(max_, prices[i] - min_)
        return max_

