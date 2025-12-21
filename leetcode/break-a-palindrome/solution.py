# First solution (beats 100%)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        _len = len(palindrome)
        if _len < 2:
            return ""
        if _len%2 == 0:
            mid = 0
        else:
            mid = _len // 2
        ret = [*palindrome]
        for i in range(_len):
            if mid > 0 and i == mid:
                continue
            if palindrome[i] != "a":
                ret[i] = "a"
                return "".join(ret)
        ret[-1] = "b"
        return "".join(ret)
