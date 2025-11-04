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

