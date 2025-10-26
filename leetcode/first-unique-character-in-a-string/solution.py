# First solution (beats 55%)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = defaultdict(int)
        for c in s:
            cache[c] += 1
        for i in range(len(s)):
            if cache[s[i]] == 1:
                return i
        return -1
