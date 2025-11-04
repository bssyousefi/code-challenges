# First solution (beats 100%)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            tmp = [1] * (i+1)
            for j in range(1, i):
                tmp[j] = ret[-1][j-1] + ret[-1][j]

            ret.append(tmp)
        return ret

