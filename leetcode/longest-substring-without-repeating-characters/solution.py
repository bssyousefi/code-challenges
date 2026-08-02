# Previous solution (beats 89%)
def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        j = 0
        m = 0
        for i in range(len(s)):
            if s[i] in cache and cache[s[i]] >= j:
                m = max(m, i-j)
                j = cache[s[i]]+1
            cache[s[i]] = i
        return max(m, len(s) - j) if m > 0 else len(s)

# Other solution (beats 62%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        _map = defaultdict(int)
        i, j = 0, 0
        while j < len(s):
            if _map[s[j]] != 0:
                if j - i > _max:
                    _max = j - i
            while _map[s[j]] != 0:

                _map[s[i]] -= 1
                i += 1

            _map[s[j]] += 1
            j += 1
        return _max if j - i < _max else j - i

# Third solution (beats 5%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        _max = 0
        for r in range(n):
            if len(set(s[l:r+1])) == r-l+1:
                _max = max(_max, r-l+1)
            else:
                l += 1
        return _max
