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

