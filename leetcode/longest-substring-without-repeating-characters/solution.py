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
