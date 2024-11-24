# First solution (beats 99%)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        i = 0
        j = len(s) -1
        while i<j:
            while i < len(s) and s[i] not in l:
                i += 1
            while j > 0 and s[j] not in l:
                j -= 1
            if i <= j and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
