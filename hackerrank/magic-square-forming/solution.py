#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    ms = [
        [[2,9,4],[7,5,3],[6,1,8]],
        [[2,7,6],[9,5,1],[4,3,8]],
        [[4,9,2],[3,5,7],[8,1,6]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[6,7,2],[1,5,9],[8,3,4]],
        [[8,1,6],[3,5,7],[4,9,2]],
        [[8,3,4],[1,5,9],[6,7,2]]
    ]
    # s_3 = (2, 4, 6, 8)
    # s_2 = (1, 3, 7, 9)
    # ms = []
    def diff(a):
        agg = 0
        for r in range(3):
            for c in range(3):
                agg += a[r][c] - s[r][c] if a[r][c] > s[r][c] else s[r][c] - a[r][c]
        return agg
        
    min_ = 81
    for a in ms:
        min_ = min(min_, diff(a))
        
    return min_
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

