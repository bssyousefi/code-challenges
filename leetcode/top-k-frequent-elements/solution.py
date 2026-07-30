# First solution (beats 70%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = defaultdict(int)
        for i in nums:
            _map[i] += 1
        ret = sorted(_map.items(), key=lambda x: x[1], reverse=True)
        return [ret[i][0] for i in range(k)]

# Second solution (beats 90%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        return sorted(counter.keys(), key=lambda x: -counter[x])[:k]

# Third solution (beats 100%) (min heap)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]
