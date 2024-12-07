# (beats 100%)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l<=r:
            m = (l+r)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1

        ll = 0
        rr = len(matrix[l-1]) - 1

        while ll <= rr:
            m = (ll+rr)//2

            if matrix[l-1][m] == target:
                return True
            elif matrix[l-1][m] < target:
                ll = m + 1
            else:
                rr = m - 1
        return False
