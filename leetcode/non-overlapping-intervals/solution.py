# First solution (beats 5%) (DP, Binary search)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        l = len(intervals)
        dp = [1] * l

        def binarySearch(k, v):
            r = l-1
            while k < r:
                m = (k+r) // 2
                if intervals[m][0] >= v:
                    r = m
                else:
                    k = m + 1
            return k

        for i in range(l-2,-1,-1):
            k = binarySearch(i+1, intervals[i][1])
            if intervals[k][0] >= intervals[i][1]:
                dp[i] = max(dp[i+1], dp[k]+1)
            else:
                dp[i] = dp[i+1]

        return l - dp[0]
# Second solution (beats 81%) (Greedy)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        l = len(intervals)
        start = float('inf')
        ret = 0
        for i in range(l-1,-1,-1):
            if intervals[i][1] > start:
                ret += 1
            else:
                start = intervals[i][0]

        return ret

# Third solution (beats 78%) (Same greedy, from left to right)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ints = sorted(intervals, key=lambda x: x[1])
        j = float("-inf")
        result = 0
        for i in range(len(ints)):
            if ints[i][0] < j:
                result += 1
            else:
                j = ints[i][1]
        return result

