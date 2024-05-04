class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = {}
        matches = 0
        k = None
        res = ''
        for i in t:
            m[i] = m.get(i,0) + 1
        
        l = 0
        n = {}
        r = l
        while r<len(s):
            if s[r] in m:
                n[s[r]] = n.get(s[r], 0) + 1
                if n[s[r]] == m[s[r]]:
                    matches += 1
            while len(m) == matches:
                if k is None or k>r-l+1:
                    k = r-l+1
                    res = s[l:r+1]
                if s[l] in m:
                    if n[s[l]] == m[s[l]]:
                        matches -= 1
                    n[s[l]] -= 1
                l += 1
            r += 1
        return res

