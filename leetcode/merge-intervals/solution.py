# First solution (beats 6%) (binary search)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = [intervals[0]]
        def insert(interval):
            nonlocal ret
            l,r = 0, len(ret)-1
            while l<=r:
                m = (l+r)//2
                if ret[m][1] < interval[0]:
                    l = m + 1
                else:
                    r = m - 1
            r = l
            while r < len(ret) and ret[r][0] <= interval[1]:
                r += 1
            if r==l:
                ret = ret[:l] + [interval] + ret[r:]
            else:
                ret = ret[:l] + [[min(interval[0], ret[l][0]), max(interval[1], ret[r-1][1])]] + ret[r:]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            insert(interval)

        return ret
# Second solution (beats 73%) (built-in sort)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        ret = []
        while i < len(intervals):
            l, r = intervals[i]
            j = i
            while i < (len(intervals)-1) and intervals[i+1][0] <= r:
                if intervals[i+1][1] > r:
                    r = intervals[i+1][1]
                i += 1
            ret.append([l, max(intervals[i][1], r)])
            i += 1
        return ret
