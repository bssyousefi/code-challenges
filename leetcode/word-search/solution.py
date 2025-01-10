# First solution (beats 92%)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.rows = len(board)
        self.cols = len(board[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0] and self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self,i, j, k):
        if k == len(self.word)-1:
            return True
        tmp = self.board[i][j]
        self.board[i][j] = "#"
        state = False
        if i > 0 and self.board[i-1][j] == self.word[k+1]:
            state = state or self.dfs(i-1, j, k+1)
        if state:
            return state
        if i < self.rows-1 and self.board[i+1][j] == self.word[k+1]:
            state = state or self.dfs(i+1, j, k+1)
        if state:
            return state
        if j > 0 and self.board[i][j-1] == self.word[k+1]:
            state = state or self.dfs(i, j-1, k+1)
        if state:
            return state
        if j < self.cols-1 and self.board[i][j+1] == self.word[k+1]:
            state = state or self.dfs(i, j+1, k+1)
        self.board[i][j] = tmp
        return state
# Another solution (beats 91%)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, k):
            if i < 0 or i == rows or j < 0 or j == cols or board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            ret = (
                dfs(i-1, j, k+1) or
                dfs(i+1, j, k+1) or
                dfs(i, j-1, k+1) or
                dfs(i, j+1, k+1)
            )
            board[i][j] = tmp
            return ret

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
