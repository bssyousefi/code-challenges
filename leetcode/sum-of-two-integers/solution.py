# First solution (beats 100%)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        res = 0
        k = 1
        mask = 0xFFFFFFFF
        while k < 1 << 32:
            la, lb = a&1, b&1
            tmp = la ^ lb ^ c
            if tmp:
                res |= k
            c = (la&c) | (lb&c) | (la&lb)
            a = a >> 1
            b = b >> 1
            k = k << 1

        # if it's a negative number, convert it to a negative number
        # in Python to compute ~x it uses -x - 1
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res
