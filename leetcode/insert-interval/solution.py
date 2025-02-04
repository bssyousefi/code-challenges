# First solution (beats 66%) (binary search)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        l, r = 0, len(intervals)-1
        while l <= r:
            m = (l+r) // 2
            if intervals[m][0] <= newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        counter = 0
        r = l
        if l > 0 and intervals[l-1][1] >= newInterval[0]:
            intervals[l-1] = [intervals[l-1][0], max(intervals[l-1][1], newInterval[1])]
            counter += 1
        while l < len(intervals) and intervals[l][0] <= newInterval[1]:
            intervals[l] = [newInterval[0], max(intervals[l][1], newInterval[1])]
            counter += 1
            l += 1

        if counter == 0:
            intervals.insert(l, newInterval)
        elif counter > 1:
            if r == 0 or intervals[r-1][1] < newInterval[0]:
                intervals[r] = [intervals[r][0], intervals[l-1][1]]
                while l-1 > r:
                    intervals.pop(l-1)
                    l -= 1
            else:
                intervals[r-1] = [intervals[r-1][0], intervals[l-1][1]]
                while l > r:
                    intervals.pop(l-1)
                    l -= 1

        return intervals
# Second solution (beats 100%) (binary search) (optimized)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        l, r = 0, len(intervals)-1
        while l <= r:
            m = (l+r) // 2
            if intervals[m][1] < newInterval[0]:
                l = m + 1
            else:
                r = m - 1
        r = l
        while r < len(intervals) and newInterval[1]>=intervals[r][0]:
            r += 1
        if l==r:
            return intervals[:l]+[newInterval]+intervals[l:]
        return intervals[:l]+[[min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[r-1][1])]] +intervals[r:]
