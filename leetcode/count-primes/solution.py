# First solution (beats 39%)
class Solution:
    def __init__(self):
        self.set = []

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        result = [1] * n
        result[0] = 0
        result[1] = 0
        print(int(n**0.5))
        for i in range(2, int(n**0.5)+1):
            if result[i] == 1 and self.isPrime(i):
                self.set.append(i)
                j = 2 * i
                while j < n:
                    result[j] = 0
                    j += i
        return sum(result)

    def isPrime(self, n: int) -> bool:
        for i in self.set:
            if n%i == 0:
                return False
        return True

