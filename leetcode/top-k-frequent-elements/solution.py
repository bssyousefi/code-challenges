# First solution (beats 70%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = defaultdict(int)
        for i in nums:
            _map[i] += 1
        ret = sorted(_map.items(), key=lambda x: x[1], reverse=True)
        return [ret[i][0] for i in range(k)]
