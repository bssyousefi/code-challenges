# First solution (beats 6%) (DP)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = (nums[-1], nums[-1], nums[-1], nums[-1])
        for i in range(len(nums)-2,-1,-1):
            a = max(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][3])
            c = min(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][3])
            b = max(a, dp[i+1][0])
            d = min(c, dp[i+1][2])
            dp[i] = (b,a,d,c)

        return dp[0][0]
# Second solution (beats 6%) (DP) (first solution with removed redundancy)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = (nums[-1], nums[-1], nums[-1])
        for i in range(len(nums)-2,-1,-1):
            a = max(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
            c = min(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
            b = max(a, dp[i+1][0])
            # d = min(c, dp[i+1][2])
            dp[i] = (b,a,c)

        return dp[0][0]
# Third solution (beats 16%) (DP) (second solution with less complexity)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = (nums[-1], nums[-1], nums[-1])
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > 0:
                a = max(nums[i], nums[i]*dp[i+1][1])
                c = nums[i]*dp[i+1][2]
                b = max(a, dp[i+1][0])
                dp[i] = (b,a,c)
            else:
                a = max(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
                c = min(nums[i], nums[i]*dp[i+1][1], nums[i]*dp[i+1][2])
                b = max(a, dp[i+1][0])
                dp[i] = (b,a,c)

        return dp[0][0]
# Fourth solution (beats 54%) (DP) (third solution with less complexity)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = (nums[-1], nums[-1], nums[-1])
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > 0:
                a = max(nums[i], nums[i]*dp[i+1][1])
                c = nums[i]*dp[i+1][2]
                b = max(a, dp[i+1][0])
                dp[i] = (b,a,c)
            else:
                if dp[i+1][1] == dp[i+1][2]:
                    a = nums[i]
                    c = nums[i] * dp[i+1][1]
                    if dp[i+1][1] <= 0:
                        a, c = c, a
                else:
                    a = nums[i] * dp[i+1][2]
                    if dp[i+1][1] > 0:
                        c = nums[i] * dp[i+1][1]
                    else:
                        c = nums[i]

                b = max(a, dp[i+1][0])
                dp[i] = (b,a,c)

        return dp[0][0]
# Fifth solution (beats 94%) (mathematical solution)
# The subarray should start at least in one end of the array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev=nums[::-1]
        for i in range(1,len(nums)):
            nums[i]*=nums[i-1] or 1
            rev[i]*= rev[i-1] or 1
        
        return max(nums+rev)
