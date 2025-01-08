# First solution (beats 85%)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        for i in range(len(candidates)):
            v = candidates[i]
            if v > target:
                continue
            elif v == target:
                ret += [[v]]
                continue
            ret += [[v, *j] for j in self.combinationSum(candidates[i:], target-v)]
        return ret

# Second solution (beats 100%) (Dynamic Programming)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target)]
        for i in candidates:
            if target < i:
                continue
            dp[i-1].append([i])
            for j in range(i, target):
                if dp[j-i]:
                    for k in dp[j-i]:
                        dp[j].append(k+[i])
        return dp[-1]
