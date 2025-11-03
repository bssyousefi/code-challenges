# First solution (beats 20%)
class Solution:
    def romanToInt(self, s: str) -> int:
        map_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        map_2 = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}
        result = 0
        l = len(s)
        for i in range(l):
            if s[i] in map_2:
                if i < l-1 and s[i+1] in map_2[s[i]]:
                    result -= map_[s[i]]
                    continue
            result += map_[s[i]]
        return result

