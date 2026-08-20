# First solution (beats 100%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        return sum([i == "1" for i in x])

# Second solution (beats 100%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        count = 0
        cur = n
        while cur:
            if cur & 1:
                count += 1
            cur = cur >> 1
        return count

# Third solution (beats 100%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


# Fourth solution (beats 100%)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # n & (n-1) will return n without its rightmost setbit
            n = n & (n-1)
            count += 1
        return count
