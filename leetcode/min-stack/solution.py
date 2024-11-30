# First solution (beats 73%)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.count = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or val < self.min[-1][1]:
            self.min.append((self.count, val))
        self.count += 1

    def pop(self) -> None:
        if self.count == (self.min[-1][0] + 1):
            self.min.pop()
        self.stack.pop()
        self.count -= 1

    def top(self) -> int:
        return self.stack[self.count - 1]

    def getMin(self) -> int:
        return self.min[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
