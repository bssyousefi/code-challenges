# First solution (beats 5%)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "a"
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "a"

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "a":
                    matrix[i][j] = 0

# Second solution (beats 100%)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_row = set()
        set_col = set()
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_col.add(j)

        for i in set_row:
            for j in range(m):
                matrix[i][j] = 0

        for j in set_col:
            for i in range(n):
                matrix[i][j] = 0
