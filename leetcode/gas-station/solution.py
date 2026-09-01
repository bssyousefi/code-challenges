# First solution (beats 47%) (logical)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        x = -1
        b = 0
        c = -1
        for i in range(len(gas)):
            tmp = gas[i] - cost[i]
            if c >= 0:
                c += tmp

            if c < 0:
                x = -1
            if x == -1 and gas[i] >= cost[i]:
                x = i
                c = tmp
            b += tmp

        if b >= 0:
            return x
        else:
            return -1

# Second solution (beats 5%) (double pointer)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        ret = -1
        gas += gas
        cost += cost
        tank = 0
        i, j = 0, 0
        while j < n and i < 2*n:
            if ret == -1 and gas[i] >= cost[i]:
                ret = i
                j = i
            if j >= n:
                return -1
            if gas[i]+tank >= cost[i]:
                tank += gas[i] - cost[i]
            else:
                ret = -1
                tank = 0
            i += 1

        return ret
