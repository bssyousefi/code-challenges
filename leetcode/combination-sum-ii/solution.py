# First solution (beats 77%)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        can = []
        i = 0
        while i < len(candidates):
            j = i
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i +=1
            for l in range(i-j+1,0,-1):
                can.append((candidates[j] * l, [candidates[j] for _ in range(l)], l))
            i += 1
        return self.cal(can, target)

    def cal(self, can, target):
        ret = []
        for i in range(len(can)):
            if can[i][0] > target:
                continue
            elif can[i][0] == target:
                ret.append(can[i][1])
            else:
                v = self.cal(can[i+can[i][2]:], target - can[i][0])
                for k in v:
                    ret.append(k+can[i][1])
        return ret

# Second soluton (93%) (better)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.cal(candidates, target)

    def cal(self, can, target):
        ret = []
        i = 0
        while i < len(can):
            if can[i] > target:
                break
            if can[i] == target:
                ret.append([can[i]])
            else:
                v = self.cal(can[i+1:], target - can[i])
                for k in v:
                    ret.append(k+[can[i]])
            while i + 1 < len(can) and can[i+1] == can[i]:
                i += 1
            i += 1
        return ret
