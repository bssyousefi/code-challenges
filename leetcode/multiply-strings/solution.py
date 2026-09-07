# First solution (beast 5%)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        _map = {str(i): i for i in range(10)}
        _sum = []
        n, m = len(num1), len(num2)
        for i in range(m-1,-1,-1):
            base_counter = (m-i-1)
            for j in range(n-1,-1,-1):
                counter = base_counter + (n-j-1) 
                val = _map[num1[j]] * _map[num2[i]]
                _sum.append(str(val) + "0"*counter)
        ret = "0"
        for i in _sum:
            ret = self.agg(ret, i)
        return ret

    def agg(self, num1: str, num2: str):
        _map = {str(i): i for i in range(10)}
        _sum = ""
        n, m = len(num1), len(num2)
        i = 0
        carry = 0
        while m > 0 or n > 0 or carry:
            val = (_map[num1[n-1]] if n > 0 else 0) + (_map[num2[m-1]] if m > 0 else 0) + carry
            _sum = str(val%10) + _sum
            carry = val//10
            m -= 1
            n -= 1
        ret = str(_sum)
        while len(ret) > 1 and ret[0] == "0":
            ret = ret[1:]
        return ret
