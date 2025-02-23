# First solution (beats 63%) (Brute force)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = defaultdict(int)
        for i in hand:
            m[i] += 1

        a = list(m.keys())
        a.sort()
        for i in a:
            if m[i] == 0:
                continue
            k = m[i]
            for j in range(groupSize):
                m[i+j] -= k
                if m[i+j] < 0:
                    return False
        return True
# Second solution (beats 67%) (min heap)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        m = {}
        a = []

        for i in hand:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
                heapq.heappush(a, i)

        while a:
            i = heapq.heappop(a)
            if m[i] == 0:
                continue
            k = m[i]
            for j in range(groupSize):
                if i+j in m and m[i+j]>=k:
                    m[i+j] -= k
                else:
                    return False
        return True
