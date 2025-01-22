# First solution (beats 37%) (max heap)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = [0]*26
        for i in tasks:
            c[ord(i)- ord('A')] += 1
        h = [-i for i in c if i > 0]
        heapq.heapify(h)
        q = []
        times = 0
        while h or q:
            if h:
                i = heapq.heappop(h)
                if i < -1:
                    q.append((i+1, times))

            if q and q[0][1] == times - n:
                v, _ = q.pop(0)
                heapq.heappush(h, v)

            times += 1

        return times
# Second solution (beats 89%) (mathematical solution)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = defaultdict(int)
        max_ = 0
        max_count = 0
        for i in tasks:
            c[i] += 1

        for i in c:
            if max_ < c[i]:
                max_ = c[i]
                max_count = 1
            elif max_ == c[i]:
                max_count += 1

        return max((max_-1)*(n+1)+max_count, len(tasks))
