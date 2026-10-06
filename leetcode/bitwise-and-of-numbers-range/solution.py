# First solution (beats 82%)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right - left + 1
        for i in range(32):
            if diff <= (1 << i):
                break

        return (left >> i << i) & (right >> i << i)

# Second solution (beats 100%)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1

        return right

# Third solution (beats 59%)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left < right:
            left >>= 1
            right >>= 1
            shifts += 1

        return left << shifts
