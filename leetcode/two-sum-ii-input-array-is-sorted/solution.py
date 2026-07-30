# First solution (beats 80%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return None

# Second solution (beats 100%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while (_sum := numbers[l] + numbers[r]) != target:
            if _sum > target:
                r -= 1
            else:
                l +=1
        return [l+1, r+1]
