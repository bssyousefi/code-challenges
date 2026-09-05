# First solution (beats 47%) (DP with memoization)
class Solution:
    def __init__(self):
        self.cache = {}
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n == 0:
            return m
        if m == 0:
            return n
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]
        if word1[0] == word2[0]:
            ret = self.minDistance(word1[1:], word2[1:])
        else:
            replace = self.minDistance(word1[1:], word2[1:])
            remove = self.minDistance(word1[1:], word2)
            insert = self.minDistance(word1, word2[1:])
            ret = 1 + min(replace, remove, insert)

        self.cache[(word1, word2)] = ret
        return ret
