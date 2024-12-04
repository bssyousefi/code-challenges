# First solution (beats 16%)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while len(stack)>0 and stack[-1][1] < temperatures[i]:
                j, _ = stack.pop()
                ret[j] = i - j
            else:
                stack.append((i, temperatures[i]))
        return ret

# Second solution (beats 64%)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while len(stack)>0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ret[j] = i - j
            else:
                stack.append(i)
        return ret
