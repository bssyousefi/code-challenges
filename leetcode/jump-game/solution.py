# First solution (beats 14%) (DFS & greedy)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = set()
        l = len(nums)
        def dfs(i):
            if i >= l:
                return False
            if i == l-1:
                return True

            for j in range(nums[i],0,-1):
                if (i+j) not in cache:
                    if dfs(i+j):
                        return True

            cache.add(i)
            return False

        return dfs(0)
# Second solution (beats 7%) (DFS & greedy - other way)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = set()
        l = len(nums)
        def dfs(i):
            if i == 0:
                return True
            for j in range(i,0,-1):
                if nums[i-j] >= j:
                    if (i-j) not in cache:
                        if dfs(i-j):
                            return True
            cache.add(i)
            return False

        return dfs(l-1)
# Third solution (beats 90%) (greedy)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1:
            return True
        for i in range(l-1):
            if nums[i] == 0:
                j = i - 1
                while j >=0 and nums[j] <= i-j:
                    j -= 1
                if j == -1:
                    return False
        return True
