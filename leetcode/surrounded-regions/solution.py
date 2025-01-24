# First solution (beats 77%) (DFS)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        d = [[False]*cols for _ in range(rows)]
        drx = ((-1,0),(0,-1),(1,0),(0,1))

        def cal(i,j):
            if i<0 or j<0 or i == rows or j == cols or d[i][j] or board[i][j] == "X":
                return
            d[i][j] = True
            for r,c in drx:
                cal(i+r, j+c)

        for i in range(rows):
            if board[i][0] == "O":
                cal(i, 0)

            if board[i][cols-1] == "O" and not d[i][cols-1]:
                cal(i, cols-1)

        for i in range(cols):
            if board[0][i] == "O" and not d[0][i]:
                cal(0, i)

            if board[rows-1][i] == "O" and not d[rows-1][i]:
                cal(rows-1, i)

        for i in range(rows):
            for j in range(cols):
                if not d[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
