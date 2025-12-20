# First solution beats(60%)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        for j in range(len(strs[0])):
            pre = strs[0][j]
            for i in range(1, len(strs)):
                if strs[i][j] < pre:
                    ret += 1
                    break
                pre = strs[i][j]

        return ret
