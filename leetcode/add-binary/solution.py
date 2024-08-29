class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        c = "0"
        r = ''
        while m>=0 or n>=0:
            s = c
            c = "0"
            if m >= 0:
                if a[m] == "1":
                    if s == "0":
                        s = "1"
                    else:
                        s = "0"
                        c = "1"
                m -= 1
            if n >= 0:
                if b[n] == "1":
                    if s == "0":
                        s = "1"
                    else:
                        s = "0"
                        c = "1"
                n -= 1
            r = s + r
        if c == "1":
            r = "1" + r
        return r


class Solution:
    def sumBinary(self, a: str, b:str, c:str) -> (str, str):
        if a == b:
            if a == "1":
                return (c, "1")
            else:
                return (c, "0")
        else:
            if c == "1":
                return ("0", c)
            else:
                return ("1", c)

    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        c = "0"
        r = ''
        while m>=0 or n>=0:
            s, c = self.sumBinary(
                a[m] if m>=0 else "0",
                b[n] if n>=0 else "0",
                c
            )
            m -= 1
            n -= 1
            r = s + r
        if c == "1":
            r = "1" + r
        return r

