# First solution (beats 92%)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        _len = len(height)
        _max = 0
        i = 0
        l = []
        r = []
        for i in range(_len):
            if len(l) == 0 or l[-1][1] < height[i]:
                l.append((i, height[i]))
            if len(r) == 0 or r[-1][1] < height[_len-1-i]:
                r.append((_len-1-i, height[_len-1-i]))

        i = 0
        j = 0
        while i < len(l) and j < len(r) and l[i][0] < r[j][0]:
            if l[i][1] < r[j][1]:
                _max = max(_max, l[i][1] * (r[j][0] - l[i][0]))
                i += 1
            else:
                _max = max(_max, r[j][1] * (r[j][0] - l[i][0]))
                j += 1
        return _max
