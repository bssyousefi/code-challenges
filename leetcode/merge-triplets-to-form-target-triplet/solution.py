# First solution (beats 8%)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = None
        for t in triplets:
            skip = False
            for i in range(3):
                if t[i] > target[i]:
                    skip = True
            if skip:
                continue
            if not cur:
                cur = t
            else:
                cur = [max(cur[i], t[i]) for i in range(3)]

        if cur is None:
            return False
        state = True
        for i in range(3):
            if target[i] != cur[i]:
                state = False
                break
        return state
# Second solution (beats 11%) (same solution)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0,0,0]
        for t in triplets:
            i = 0
            while i < 3:
                if t[i] > target[i]:
                    break
                i += 1
            if i < 3:
                continue
            cur = [max(cur[i], t[i]) for i in range(3)]
        if cur == target:
            return True
        return False
# Third solution (beats 79%) (same solution-optimized)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0,0,0]
        for t in triplets:
            i = 0
            newCur = [0,0,0]
            while i < 3:
                newCur[i] = max(cur[i], t[i])
                if t[i] > target[i]:
                    break
                i += 1
            if i < 3:
                continue
            cur = newCur
            if cur == target:
                return True
        return False
