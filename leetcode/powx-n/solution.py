# First solution (beats 100%)
    class Solution:
    def __init__(self):
        self.cache = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        if n%2==0:
            val = self.myPow(x,n//2)
            self.cache[n] = val * val
        else:
            self.cache[n] = self.myPow(x,n//2) * self.myPow(x, n-n//2)

        return self.cache[n]
