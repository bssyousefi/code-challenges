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

