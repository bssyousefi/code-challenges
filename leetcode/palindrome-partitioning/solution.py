# First (beats 97%)
class Solution:
    def __init__(self):
        self.cache = {}

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        ret = []
        for i in range(len(s)):
            if self.isPalindrome(s[0:i+1]):
                if s[i+1:] in self.cache:
                    v = self.cache[s[i+1:]]
                else:
                    v = self.partition(s[i+1:])
                    self.cache[s[i+1:]] = v
                for k in v:
                    ret.append([s[0:i+1]] + k)
        return ret


    def isPalindrome(self, s:str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
