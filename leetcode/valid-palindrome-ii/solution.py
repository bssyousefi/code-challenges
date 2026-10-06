# First solution (beats 97%) (2 pointer)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(word) -> bool:
            return word == word[::-1]
        if isPalindrome(s):
            return True

        n = len(s)
        i = 0
        while i < n//2:
            if s[i] != s[n-1-i]:
                if isPalindrome(s[:i]+s[i+1:]):
                    return True
                if isPalindrome(s[:n-1-i]+s[n-i:]):
                    return True
                return False
            i += 1
        return False
