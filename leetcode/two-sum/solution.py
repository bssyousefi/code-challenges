class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        for i in range(len(nums)):
            if nums[i] in _map:
                return [_map[nums[i]], i]
            else:
                _map[target - nums[i]] = i
        return [-1, -1]
