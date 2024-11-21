# First solution that I've got
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        while i < len(p)-3:
            if p[i] != "*" and p[i+1] == "*":
                if p[i] == p[i+2] and p[i+3] == "*":
                    p = p[:i] + p[i:i+2] + p[i+4:]
            i += 1
        p_size = len(p)
        s_size = len(s)
        if p_size == 0 and s_size == 0:
            return True
        if p_size == 0:
            return False
        i = 0
        j = 0
        if p[j] == ".":
            if (j < p_size - 1) and p[j+1] == "*":
                if s_size == 0:
                    return self.isMatch(s, p[j+2:])
                ret = self.isMatch(s[i+1:], p[j:])
                if ret:
                    return ret
                ret2 = self.isMatch(s[i:], p[j+2:])
                ret = ret or ret2
            else:
                if s_size == 0:
                    return False
                ret = self.isMatch(s[i+1:], p[j+1:])
        elif p[j] != "*":
            if s_size == 0:
                if (j < p_size - 1) and p[j+1] == "*":
                    return self.isMatch(s, p[j+2:])
                else:
                    return False
            elif s[i] == p[j]:
                if (j < p_size - 1) and p[j+1] == "*":
                    ret = self.isMatch(s[i+1:], p[j:])
                    if ret:
                        return ret
                    ret2 = self.isMatch(s[i:], p[j+2:])
                    ret = ret or ret2
                else:
                    ret = self.isMatch(s[i+1:], p[j+1:])
            else:
                if (j < p_size - 1) and p[j+1] == "*":
                    ret = self.isMatch(s[i:], p[j+2:])
                else:
                    ret = False
        return ret

# Second solution is same as the first + cache (beats 94%)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        self.cache = {}
        while i < len(p)-3:
            if p[i] != "*" and p[i+1] == "*":
                if p[i] == p[i+2] and p[i+3] == "*":
                    p = p[:i] + p[i:i+2] + p[i+4:]
            i += 1
        return self.check(s, p)
    def check(self, s:str, p:str) -> bool:
        if (s,p) in self.cache:
            return self.cache[(s,p)]
        p_size = len(p)
        s_size = len(s)
        if p_size == 0 and s_size == 0:
            return True
        if p_size == 0:
            return False
        i = 0
        j = 0
        if p[j] == ".":
            if (j < p_size - 1) and p[j+1] == "*":
                if s_size == 0:
                    return self.check(s, p[j+2:])
                ret = self.check(s[i+1:], p[j:])
                if ret:
                    return ret
                ret2 = self.check(s[i:], p[j+2:])
                ret = ret or ret2
            else:
                if s_size == 0:
                    return False
                ret = self.check(s[i+1:], p[j+1:])
        elif p[j] != "*":
            if s_size == 0:
                if (j < p_size - 1) and p[j+1] == "*":
                    return self.check(s, p[j+2:])
                else:
                    return False
            elif s[i] == p[j]:
                if (j < p_size - 1) and p[j+1] == "*":
                    ret = self.check(s[i+1:], p[j:])
                    if ret:
                        return ret
                    ret2 = self.check(s[i:], p[j+2:])
                    ret = ret or ret2
                else:
                    ret = self.check(s[i+1:], p[j+1:])
            else:
                if (j < p_size - 1) and p[j+1] == "*":
                    ret = self.check(s[i:], p[j+2:])
                else:
                    ret = False
        self.cache[(s,p)] = ret
        return ret
    
