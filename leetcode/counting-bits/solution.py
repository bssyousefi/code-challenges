# First solution (beats 26%) (set bit remover)
class Solution:
    def countBits(self, n: int) -> List[int]:
        def oneCounter(i):
            count = 0
            while i:
                i = i & (i-1)
                count += 1
            return count
        return [oneCounter(i) for i in range(n+1)]

# Second solution (beats 95%) (dynamic programming)
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n+1)
        for i in range(1,n+1):
            if i%2==0:
                ret[i] = ret[i//2]
            else:
                ret[i] = ret[i//2] + 1
        return ret
