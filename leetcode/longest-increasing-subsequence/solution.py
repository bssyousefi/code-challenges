# First solution (beats 70%) (DP) (959 ms)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [1] * l
        ret = 1
        for i in range(l-1,-1,-1):
            for j in range(i+1, l):
                if nums[i] < nums[j] and dp[i]<(dp[j]+1):
                    dp[i] = dp[j]+1
                    if ret < dp[i]:
                        ret = dp[i]
        return ret
# Second solution (beats 96%) (built-in bisect) (3 ms)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        arr = []
        for i in range(l):
            idx = bisect.bisect_left(arr, nums[i])
            if idx == len(arr):
                arr.append(nums[i])
            else:
                arr[idx] = nums[i]
        return len(arr)
