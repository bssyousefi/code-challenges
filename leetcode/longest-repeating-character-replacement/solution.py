# Previous solution (beats 61%)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        m = 0
        l = 0
        for i in range(len(s)):
            cache[s[i]] = cache.get(s[i],0) + 1
            m = max(m, cache[s[i]])
            if (i-l+1 - m) > k:
                cache[s[l]] -= 1
                l += 1

        return i-l+1

# Second solution (beats 94%)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        _max = 0
        _map = defaultdict(int)
        n = len(s)
        l, r = 0, 0
        m = 0
        while r < n:
            _map[s[r]] += 1
            if _map[s[r]] > m:
                m = _map[s[r]]
            if r-l+1-k > m:
                _map[s[l]] -= 1
                l += 1

            if r-l+1 > _max:
                _max = r-l+1
            r += 1

        return _max
