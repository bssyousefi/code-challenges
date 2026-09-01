# First solution (Beats 100%)
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n > 1:
            if n in cache:
                return False
            cache.add(n)
            _sum = 0
            x = n
            while x:
                _sum += (x%10)**2
                x = x // 10
            n = _sum

        return True
