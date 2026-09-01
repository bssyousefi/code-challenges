# First solution (beats 5%) (BFS using Python list comprehension) (Comments timed out)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # q = [(0,0)]
        q = [0]
        ret = 0
        counter = 0
        while counter < n:
            res = [m+nums[counter] for m in q]
            res += [m-nums[counter] for m in q]
            q = res
            counter += 1

        return sum([m==target for m in q])
        # while q:
        #     res = []
        #     for i, s in q:
        #         if i == n:
        #             if s == target:
        #                 ret += 1
        #         else:
        #             res.extend([(i+1, s+nums[i]), (i+1, s-nums[i])])
        #     q = res
        # while q:
        #     for _ in range(len(q)):
        #         i, s = q.pop(0)
        #         if i == n:
        #             if s == target:
        #                 ret += 1
        #         else:
        #             q.extend([(i+1, s+nums[i]), (i+1, s-nums[i])])
        return ret
        # def dfs(i, s):
        #     if i == n:
        #         if s == target:
        #             return 1
        #         return 0
        #     ret = 0
        #     ret += dfs(i+1, s+nums[i])
        #     ret += dfs(i+1, s-nums[i])
        #     return ret

        # return dfs(0,0)

