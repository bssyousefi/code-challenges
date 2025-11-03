# First solution (beats 100%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        return sum([i == "1" for i in x])
