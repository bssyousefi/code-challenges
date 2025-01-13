# First solution (beats 100%)
class Solution:
    def __init__(self):
        self.cache = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ret = []
        v = self.letterCombinations(digits[1:])
        for j in self.cache[digits[0]]:
            if not v:
                ret.append(j)
            else:
                for i in v:
                    ret.append(j + i)
        return ret
