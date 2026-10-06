# First solution (beats 67%) (min heap)
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        size = 0
        drops = [] # loc, pax
        for trip in trips:
            while drops and drops[0][0] <= trip[1]:
                _, c = heapq.heappop(drops)
                size -= c

            size += trip[0]
            if size > capacity:
                return False

            heapq.heappush(drops, (trip[2], trip[0]))

        return True
