# First solution (beats 100%)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = bin(x ^ y)
        return sum([i == "1" for i in z])
