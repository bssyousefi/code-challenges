# First solution (beats 65%)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()
        for i in nums:
            if i in cache:
                cache.remove(i)
            else:
                cache.add(i)

        return list(cache)[0]

# Second solution (beats 100%)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

