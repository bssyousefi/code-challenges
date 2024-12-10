# Previous solution (beats 67%)
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

# Other solution (beats 38%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        i,j = 0, 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                _max = max(_max, prices[j] - prices[i])
            j += 1
        return _max

# Third solution (beats 92%)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = 1e7
        max_ = 0
        for price in prices:
            if price < min_:
                min_ = price
            elif price - min_ > max_:
                max_ = price - min_
        return max_
