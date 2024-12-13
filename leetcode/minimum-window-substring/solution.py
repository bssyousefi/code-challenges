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
# Second soluton (beats 70%)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        _min = (1e6,-1,-1)
        _map = defaultdict(int)
        cache = defaultdict(int)
        count = 0
        n = len(t)
        for i in t:
            _map[i] += 1

        i,j = 0, 0
        while j < len(s):
            if count != n:
                if _map[s[j]] > 0:
                    cache[s[j]] += 1
                    if cache[s[j]] <= _map[s[j]]:
                        count += 1
                while count == n:
                    if j - i < _min[0]:
                        _min = (j-i+1, i, j)
                    if _map[s[i]] > 0:
                        if cache[s[i]] <= _map[s[i]]:
                            count -= 1
                        cache[s[i]] -= 1
                    i += 1
                j += 1

        return s[_min[1]:_min[2]+1]
