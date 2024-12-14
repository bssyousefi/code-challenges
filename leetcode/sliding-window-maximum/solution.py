# First solution (beats 5%) (better than 2nd)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxs = []
        m = -1e7
        l = 0
        r = 0
        while r < len(nums):
            while maxs and nums[maxs[-1]] < nums[r]:
                maxs.pop(-1)
            maxs.append(r)

            if l > maxs[0]:
                maxs.pop(0)

            if r>=k-1:
                res.append(nums[maxs[0]])
                l += 1
            r += 1
        
        return res

# Second solution (beats 5%)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        _max = []
        res = []
        for r in range(k):
            while len(_max) > 0 and nums[r] > _max[-1]:
                _max.pop(-1)
            _max.append(nums[r])
        res = [_max[0]]
        l = 0
        while r < len(nums) - 1:
            if nums[l] == _max[0]:
                _max.pop(0)
            l += 1
            r += 1
            while len(_max) > 0 and nums[r] > _max[-1]:
                _max.pop(-1)
            _max.append(nums[r])
            res.append(_max[0])

        return res

# Third solution (beats 43%) (use deque)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxs = deque()
        m = -1e7
        l = 0
        r = 0
        while r < len(nums):
            while maxs and nums[maxs[-1]] < nums[r]:
                maxs.pop()
            maxs.append(r)

            if l > maxs[0]:
                maxs.popleft()

            if r>=k-1:
                res.append(nums[maxs[0]])
                l += 1
            r += 1
        
        return res
