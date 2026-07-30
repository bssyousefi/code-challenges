# First solution (beats 90%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _map = defaultdict(set)
        for i in range(9):
            s = set()
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in s:
                    return False
                else:
                    s.add(v)
                if v in _map[j]:
                    return False
                else:
                    _map[j].add(v)
                if v in _map[f'{i//3}-{j//3}']:
                    return False
                else:
                    _map[f'{i//3}-{j//3}'].add(v)
        return True

# Second solution (beats 81%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for i in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rows[row]:
                    return False
                else:
                    rows[row].add(val)

                if val in cols[col]:
                    return False
                else:
                    cols[col].add(val)

                if val in squares[row//3][col//3]:
                    return False
                else:
                    squares[row//3][col//3].add(val)
        return True

# Third solution (beats 100%)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if (value:= board[row][col]) in "0123456789":
                    if value in rows[row] or value in cols[col] or value in squares[3*(row//3)+col//3]:
                        return False
                    else:
                        rows[row].add(value)
                        cols[col].add(value)
                        squares[3*(row//3)+col//3].add(value)
        return True
