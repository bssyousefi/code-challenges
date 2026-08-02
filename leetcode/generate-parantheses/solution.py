# First solution (beats 100%) (BFS)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        q = [(n-1,n, "(")]
        while q:
            i, j, s = q.pop(0)
            if i > 0:
                q.append((i-1, j, s+"("))
            elif j == 0:
                ret.append(s)
            if j > 0 and j > i:
                q.append((i, j-1, s+")"))
        return ret

# Second solution (beats 100%) (DFS)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(word, balance, rem):
            if balance == rem == 0:
                ret.append(word)
                return
            if rem > 0:
                dfs(word+"(", balance+1, rem-1)
            if balance > 0:
                dfs(word+")", balance-1, rem)
        dfs("", 0, n)
        return ret
