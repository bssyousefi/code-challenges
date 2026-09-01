# First solution (beats 100%)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, left = 0, 0
        right, bottom = n-1, m-1
        ret = []
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ret.append(matrix[top][i])
            top += 1

            if top > bottom:
                break

            for i in range(top,bottom+1):
                ret.append(matrix[i][right])

            right -= 1

            if left > right:
                break

            for i in range(right, left-1, -1):
                ret.append(matrix[bottom][i])

            bottom -= 1

            if bottom < top:
                break

            for i in range(bottom,top-1,-1):
                ret.append(matrix[i][left])

            left += 1

            if left > right:
                break

        return ret
