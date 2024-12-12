class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = {}
        for i in s1:
            m[i] = m.get(i, 0) + 1

        i = 0
        while i<len(s2):
            if s2[i] in m:
                j = i
                n = {}
                while j<len(s2):
                    if s2[j] in m:
                        if m[s2[j]] > n.get(s2[j], 0):
                            n[s2[j]] = n.get(s2[j], 0) + 1
                            if j-i+1 == len(s1):
                                if n == m:
                                    return True
                                else:
                                    n[s2[i]] -= 1
                                    i += 1
                            j += 1
                        else:
                            n[s2[i]] -= 1
                            i += 1
                    else:
                        i = j + 1
                        break
                if j == len(s2):
                    break
            else:
                i += 1

        return False

# New solution (beats 70%)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _map = {}
        for s in s1:
            _map[s] = _map.get(s, 0) + 1

        i, j = 0, 0
        while j < len(s2):
            if _map.get(s2[j], 0) > 0:
                _map[s2[j]] -= 1

                if j - i + 1 == len(s1):
                    return True
                j += 1
            else:
                while _map.get(s2[j], 0) == 0 and i < j:
                    _map[s2[i]] += 1
                    i += 1
            if i == j:
                while j < len(s2) and _map.get(s2[j], 0) == 0:
                    j += 1
                i = j
        return False
