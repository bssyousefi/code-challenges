# First solution (beats 98%)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        sums = set()
        subs = set()
        ret = []
        board = [["."]*n for _ in range(n)]

        def cal(m):
            if m == -1:
                ret.append(["".join(board[i]) for i in range(n)])
            for i in range(n):
                if i not in cols and (i+m) not in sums and (i-m) not in subs:
                    cols.add(i)
                    sums.add(i+m)
                    subs.add(i-m)
                    board[m][i] = "Q"
                    cal(m-1)
                    board[m][i] = "."
                    cols.remove(i)
                    sums.remove(i+m)
                    subs.remove(i-m)
        cal(n-1)
        return ret
