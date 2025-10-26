# First solution (beats 100%)
class Solution:
    def myAtoi(self, s: str) -> int:
        max_ = (1<<31) - 1
        max_t = max_ // 10
        max_d = max_ % 10
        i = 0
        l = len(s)
        chars = "0123456789"
        map_ = {chars[i]: i for i in range(10)}
        while i < l:
            if s[i] == " ":
                i += 1
            else:
                break
        sign = 1
        if i == l:
            return 0
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        result = 0
        while i < l:
            if s[i].isnumeric():
                if result > max_t:
                    result = max_ if sign == 1 else max_ + 1
                    break
                elif result == max_t:
                    if sign == 1 and map_[s[i]] > max_d:
                        result = max_
                        break
                    elif sign == -1 and map_[s[i]] > (max_d+1):
                        result = max_ + 1
                        break

                result = result * 10 + map_[s[i]]
                i += 1
            else:
                break
        return result * sign
