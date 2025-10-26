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

# Second solution (beats 100%)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            while result:
                if strs[i].startswith(result):
                    break
                else:
                    result = result[:-1]
        return result

