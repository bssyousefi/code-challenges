class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        i = 0
        l = len(strs)
        if l == 1:
            return strs[0]
        while True:
            if i == len(strs[0]):
                break
            r = strs[0][i] if len(strs[0]) > 0 else ""
            j = 1
            while j < l:
                if i < len(strs[j]) and r == strs[j][i]:
                    pass
                else:
                    break
                j += 1
            if j != l:
                break
            s += r
            i += 1
        return s

