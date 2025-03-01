# First solution (beats 54%)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = defaultdict(int)
        for i in s:
            m[i] += 1

        ret = []
        c = set()
        start = 0
        for i in range(len(s)):
            c.add(s[i])
            m[s[i]] -= 1
            if m[s[i]] == 0:
                c.remove(s[i])
                if len(c) == 0:
                    ret.append(i-start+1)
                    start = i + 1
        return ret
# Second solution (beats 90%) (same solution)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = defaultdict(int)
        for i in s:
            m[i] += 1

        ret = []
        c = set()
        start = 0
        for i in range(len(s)):
            if s[i] not in c:
                c.add(s[i])
            m[s[i]] -= 1
            if m[s[i]] == 0:
                c.remove(s[i])
                if len(c) == 0:
                    ret.append(i-start+1)
                    start = i + 1
        return ret
# Third solution (beats 94%) (Different approach)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {j: i for i,j in enumerate(s)}

        ret = []
        start = 0
        end = 0
        for i,j in enumerate(s):
            if end < m[j]:
                end = m[j]

            if i == end:
                ret.append(end-start+1)
                start = i + 1

        return ret
