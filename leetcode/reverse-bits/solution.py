# First solution (beats 37%)
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f"{bin(n)[:1:-1]:0<32}", 2)

# Second solution (beats 90%)
class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[:1:-1]
        if len(x) < 32:
            x += "0" * (32-len(x))
        return int(x, 2)

# Third solution (beats 58%)
class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        count = 0
        while n:
            ret ^= n & 1
            n = n >> 1
            ret = ret << 1
            count += 1
        while count < 31:
            ret = ret << 1
            count += 1
        return ret
