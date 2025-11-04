# First solution (beats 100%)
class Solution:
    def checkValidString(self, s: str) -> bool:
        c = 0
        n = 0
        for i in s:
            if i == "*":
                n += 1
            elif i == "(":
                c += 1
            elif i == ")":
                c -= 1

            if c < 0:
                if n + c < 0:
                    return False

        if c < 0 and n+c < 0:
            return False
        elif c > 0 and c-n > 0:
            return False

        c = 0
        n = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "*":
                n += 1
            elif s[i] == ")":
                c += 1
            elif s[i] == "(":
                c -= 1

            if c < 0:
                if n + c < 0:
                    return False

        if c < 0 and n+c < 0:
            return False
        elif c > 0 and c-n > 0:
            return False
        return True
# Second solution (beats 100%) (better one)
class Solution:
    def checkValidString(self, s: str) -> bool:
        open = 0
        close = 0
        l = len(s)

        for i in range(l):
            if s[i] == '(' or s[i] == '*':
                open += 1
            else:
                open -= 1

            if s[l-i-1] == ')' or s[l-i-1] == '*':
                close += 1
            else:
                close -= 1

            if open < 0 or close < 0:
                return False

        return True
