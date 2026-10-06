# First solution (beats 6%)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        _map = defaultdict(int)
        ret = [-1, 0]
        for num in nums:
            _map[num] += 1
            if _map[num] > ret[1]:
                ret = [num, _map[num]]

        return ret[0]

# Second solution (beats 76%) (same solution)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        _map = Counter(nums)
        ret = [-1, 0]
        for i,j in _map.items():
            if j > ret[1]:
                ret = [i, j]
        
        return ret[0]

# Third solution (beats 100%) (sort)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
