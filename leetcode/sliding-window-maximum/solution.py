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

