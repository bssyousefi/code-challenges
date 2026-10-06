# First solution (beats 88%) (stack)
class StockSpanner:

    def __init__(self):
        self.data = []
        self.stack = []

    def next(self, price: int) -> int:
        self.data.append(price)
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        ret = len(self.data)-self.stack[-1][0]-1 if self.stack else len(self.data)
        self.stack.append((len(self.data)-1, price))
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
