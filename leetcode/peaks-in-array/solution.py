# First solution (beats 62%)
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        peaks = set()
        peaks_sorted = []
        answer = []
        ll = len(nums)
        def find_peak(i):
            l,r = 0, len(peaks_sorted)-1
            while l <= r:
                m = (l+r) // 2
                if i < peaks_sorted[m]:
                    r = m - 1
                elif i > peaks_sorted[m]:
                    l = m + 1
                else:
                    return m
            return l

        def update_peaks(i):
            if 0 < i < ll-1:
                if nums[i-1] < nums[i] > nums[i+1]:
                    if i not in peaks:
                        loc = find_peak(i)
                        peaks_sorted.insert(loc, i)
                        peaks.add(i)
                elif i in peaks:
                    peaks.remove(i)
                    loc = find_peak(i)
                    peaks_sorted.pop(loc)

        for i in range(1, len(nums)-1):
            update_peaks(i)

        for query in queries:
            if query[0] == 2:
                nums[query[1]] = query[2]
                for i in {query[1], query[1]-1, query[1]+1}:
                    update_peaks(i)
            elif query[0] == 1:
                l = find_peak(query[1])
                r = find_peak(query[2])
                sum_ = r-l-1
                if l < len(peaks_sorted) and peaks_sorted[l] == query[1]:
                    if l == r:
                        sum_ += 1
                else:
                    sum_ += 1
                answer.append(sum_)

        return answer
