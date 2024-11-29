# First solution (beats 100%)
class Solution:
    def isValid(self, s: str) -> bool:
        _map = {"(": ")", "[": "]", "{": "}"}
        _stack = []
        for i in s:
            if i in _map:
                _stack.append(_map[i])
            else:
                if len(_stack) == 0 or _stack.pop() != i:
                    return False
        return len(_stack) == 0
