# First solution (beats 65%) (3ms)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                v2 = _stack.pop()
                v1 = _stack.pop()
                _stack.append(self.evaluate(v1, v2, token))
            else:
                _stack.append(int(token))
        return _stack.pop()

    def evaluate(self, a: int, b: int, op: str):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a // b if a * b > 0 else -(abs(a) // abs(b))

# Second solution (beats 100%) (0ms) (Remove function call)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        for token in tokens:
            if token == "+":
                _stack.append(_stack.pop() + _stack.pop())
            elif token == "-":
                _stack.append(-_stack.pop() + _stack.pop())
            elif token == "*":
                _stack.append(_stack.pop() * _stack.pop())
            elif token == "/":
                _stack.append(int(1/_stack.pop() * _stack.pop()))
            else:
                _stack.append(int(token))
        return _stack.pop()
