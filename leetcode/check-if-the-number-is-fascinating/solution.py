class Solution:
    def isFascinating(self, n: int) -> bool:
        B = list(map(str, range(1,10)))
        ns = (n, 2*n, 3*n)
        for A in ns:
            A = str(A)
            if len(A) != 3:
                return False
            for i in A:
                if i not in B:
                    return False
                else:
                    B.remove(i)
        return True
