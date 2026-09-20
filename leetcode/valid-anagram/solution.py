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

# Second solution (beats 43%) (Hashmap)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return not any(counter.values())

# Third solution (beats 92%) (hashmap)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
