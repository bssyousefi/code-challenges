# First solution (beats 59%)
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x *= sign
        result = 0
        while x > 0:
            mod, x = x%10, x//10
            result = result * 10 + mod
        if result > 1<<31:
            result = 0
        elif result == 1<<31 and sign > 1:
            result = 0
        return result * sign

# Second solution (beats 32%) (not int64)
class Solution:
    def reverse(self, x: int) -> int:
        max = 1<<31
        max_t = max//10
        max_d = max%10
        if x >= 0:
            sign = 1
        else:
            sign = -1
        x *= sign
        result = 0
        while x > 0:
            mod, x = x%10, x//10
            if result > max_t:
                return 0
            elif result == max_t:
                if sign == 1 and mod > max_d:
                    return 0
                elif sign == -1 and mod > (max_d+1):
                    return 0
            result = result * 10 + mod

        return result * sign
