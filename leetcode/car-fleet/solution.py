# First solution (beats 30%)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = [((target-position[i])/speed[i], position[i]) for i in range(len(speed))]
        n = sorted(n, key=lambda x: x[1], reverse=True)
        _min = n[0][0]
        count = 1
        for i in range(1, len(n)):
            if n[i][1] == n[i-1][1]:
                pass
            if n[i][0] > _min:
                count += 1
                _min = n[i][0]
            else:
                _min = _min if n[i][0] < _min else n[i][0]
        return count

# Second solution (beats 87%) (removed extra blocks)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = [((target-position[i])/speed[i], position[i]) for i in range(len(speed))]
        n = sorted(n, key=lambda x: x[1], reverse=True)
        _min = n[0][0]
        count = 1
        for i in range(1, len(n)):
            if n[i][0] > _min:
                count += 1
                _min = n[i][0]
        return count
