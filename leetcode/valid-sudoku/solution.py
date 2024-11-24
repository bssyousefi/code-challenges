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
