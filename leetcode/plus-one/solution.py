# First solution (beats 100%)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self._plusOne(digits, len(digits)-1)

    def _plusOne(self, digits: List[int], index: int) -> List[int]:
        if index == -1:
            return [1, *digits]
        if digits[index] == 9:
            digits[index] = 0
            return self._plusOne(digits, index-1)
        else:
            digits[index] += 1
            return digits
