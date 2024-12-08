# First solution (beats 5%)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        j = max(piles)
        i = 1
        _min = j
        while i <= j:
            m = (i + j) // 2
            v = self.calculate(piles, m)
            print(i, j, m, v)
            if v > h:
                i = m + 1
            else:
                _min = min(_min, m)
                j = m - 1
        return _min

    def calculate(self, piles, m):
        n = [i // m for i in piles]
        n = [n[i] + (1 if piles[i]-(n[i]*m)>0 else 0) for i in range(len(piles))]
        return sum(n)

# Previous solution (beats 18%)
class Solution:
    def getMoves(self, piles, k):
        n = 0
        for i in piles:
            n += i//k
            n += 0 if i%k==0 else 1
        return n
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = None
        min_ = 1
        for s in piles:
            if max_ is None:
                max_ = s
            else:
                max_ = max(max_, s)
        while min_<max_:
            m = (min_+max_)//2
            n = self.getMoves(piles, m)

            if n <= h:
                max_ = m
            else:
                min_ = m + 1
        return int(min_)

# Thirs solution (beats 90%) (use math.ceil)
class Solution:
    def getMoves(self, piles, k):
        return sum([ceil(i/k) for i in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = None
        min_ = 1
        for s in piles:
            if max_ is None:
                max_ = s
            else:
                max_ = max(max_, s)
        while min_<max_:
            m = (min_+max_)//2
            n = self.getMoves(piles, m)

            if n <= h:
                max_ = m
            else:
                min_ = m + 1
        return int(min_)
