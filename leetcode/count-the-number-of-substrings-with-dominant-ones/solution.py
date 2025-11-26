# First solution (Time exceeded)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            m = 0
            for j in range(i, len(s)):
                m += 1 if s[j] == "1" else 0
                if m > 0 and m >= (j-i-m+1)**2:
                    ret += 1

        return ret

# Second solution (Better, but still time exceeded)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ret = 0
        l = len(s)
        max_ = ((-1 + math.sqrt(1 + 4 * l)) // 2)+1
        cache = {}
        def getCache(i):
            if i not in cache:
                cache[i] = i * i
            return cache[i]

        for i in range(l):
            m = 0
            for j in range(i, l):
                m += 1 if s[j] == "1" else 0
                if (j-i+1-m > max_):
                    break
                if m > 0 and m >= getCache(j-i-m+1):
                    ret += 1

        return ret

# Third solution (Beats 16%)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ret = 0
        max_ = int((-1 + math.sqrt(1+4*len(s)))//2)+1
        for zero in range(max_):
            zeros = 0
            ones = 0
            l = 0
            last_invalid = -1
            for r in range(len(s)):
                if s[r] == "0":
                    zeros += 1
                else:
                    ones += 1

                while l < r:
                    if s[l] == "0" and zeros > zero:
                        zeros -= 1
                        last_invalid = l
                        l += 1
                    elif s[l] == "1" and (ones - 1) >= zero * zero:
                        ones -= 1
                        l += 1
                    else:
                        break

                if zeros == zero and ones >= zero * zero:
                    ret += (l - last_invalid)

        return ret
