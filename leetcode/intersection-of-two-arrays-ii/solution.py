# First solution (beats 100%)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        result = []
        for i in nums1:
            map1[i] += 1

        for i in nums2:
            map2[i] += 1

        for i in map1:
            if i in map2:
                result += min(map1[i], map2[i]) * [i]

        return result
