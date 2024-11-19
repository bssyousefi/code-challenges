class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _map = defaultdict(int)
        for i in s:
            _map[i] += 1
        for i in t:
            if i not in _map:
                return False
            _map[i] -= 1
            if _map[i] < 0:
                return False
        return True
