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
