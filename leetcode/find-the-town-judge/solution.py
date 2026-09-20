# First solution (beats 95%) (hash map)
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        candidates = {i+1:0 for i in range(n)}
        for truster, trustee in trust:
            if trustee in candidates:
                candidates[trustee] += 1
            if truster in candidates:
                del candidates[truster]

        for candidate, trusters in candidates.items():
            if trusters == n - 1:
                return candidate

        return -1
