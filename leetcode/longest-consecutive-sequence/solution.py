# First solution (beats 70%, but is not O(n))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        _max = 1
        cur = 1
        s = sorted(nums)
        for i in range(1,len(nums)):
            if s[i] == s[i-1] + 1:
                cur += 1
                if cur > _max:
                    _max = cur
            elif s[i] == s[i-1]:
                pass
            else:
                cur = 1
        return _max


# Second solution (O(n), if uncomment beats(85%))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)
        _max = 0
        for i in nums:
            if i-1 not in _set:
                cur = 1
                while i + 1 in _set:
                    cur += 1
                    i += 1
                else:
                    if cur > _max:
                        _max = cur
                # if _max > len(_set)//2:
                #     return _max
        return _max
