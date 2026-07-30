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

# Third solution (beats 5%) (some stupid solution)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        _max = [(n-1, temperatures[n-1])]
        for i in range(n-2, -1, -1):
            if _max and temperatures[i] >= _max[-1][1]:
                while _max and temperatures[i] >= _max[-1][1]:
                    _max.pop(-1)
                if len(_max) > 0:
                    ret[i] = _max[-1][0] - i
                _max.append((i, temperatures[i]))
            else:
                ret[i] = _max[-1][0] - i
                _max.append((i, temperatures[i]))
        return ret
