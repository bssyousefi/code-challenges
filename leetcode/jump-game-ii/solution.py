## First solution (times out) (BFS)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0

        q = list(range(nums[0],0,-1))
        steps = 0
        while q:
            lq = len(q)
            steps += 1
            for _ in range(lq):
                i = q.pop(0)
                if i >= l - 1:
                    return steps
                else:
                    q.extend(range(i+nums[i],0,-1))

        return -1
# Second solution (times out) (BFS-backward)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0

        q = [l-1-i for i in range(l-1,0,-1)if nums[l-1-i]>=i]
        steps = 0
        while q:
            lq = len(q)
            steps += 1
            for _ in range(lq):
                i = q.pop(0)
                if i == 0:
                    return steps
                else:
                    q.extend([i-j for j in range(i,0,-1) if nums[i-j]>=j])

        return -1
# Third solution (beats 5%) (BFS-backward-memoized)
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        cache = set()
        if l == 1:
            return 0

        q = [l-1-i for i in range(l-1,0,-1)if nums[l-1-i]>=i]
        cache.update(q)
        steps = 0
        while q:
            lq = len(q)
            steps += 1
            for _ in range(lq):
                i = q.pop(0)
                cache.add(i)
                if i == 0:
                    return steps
                else:
                    tmp = [i-j for j in range(i,0,-1) if nums[i-j]>=j and (i-j) not in cache]
                    cache.update(tmp)
                    q.extend(tmp)

        return -1
# Fourth solution (beats 90%) (greedy)

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        max_ = 0
        steps = 0
        end = 0
        for i in range(l-1):
            if i + nums[i] > max_:
                max_ = i + nums[i]
                if max_ >= l - 1:
                    return steps + 1
            if i == end:
                steps += 1
                end = max_
        return steps
