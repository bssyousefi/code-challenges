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

# Third solution (beats 100%)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = strs[0]

        def find(a, b):
            n, m = len(a), len(b)
            i = 0
            while i < n and i < m:
                if a[i] == b[i]:
                    i += 1
                else:
                    break
            return a[:i]

        n = len(strs)
        for i in range(1, n):
            ret = find(ret, strs[i])
            if ret == "":
                return ""
        return ret
