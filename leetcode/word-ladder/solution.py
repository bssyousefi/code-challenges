# First solution (beats 5%) (Brute-force + BFS)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isRelated(w1, w2):
            if len(w1) != len(w2):
                return False
            counter = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    counter += 1
                    if counter > 1:
                        return False
            return True if counter == 1 else False

        l = len(wordList)
        visit = [False] * (l+1)
        d = defaultdict(list)
        begin, end = -1, -1
        for i in range(l):
            if begin <0 and wordList[i] == beginWord:
                begin = i
            if end <0 and wordList[i] == endWord:
                end = i
            for j in range(i, l):
                if i != j and isRelated(wordList[i], wordList[j]):
                    d[i].append(j)
                    d[j].append(i)

        if begin < 0:
            begin = l
            for i in range(l):
                if isRelated(beginWord, wordList[i]):
                    d[begin].append(i)

        q = deque()
        q.append((begin,1))

        while q:
            i, counter = q.popleft()
            visit[i] = True
            if i == end:
                return counter
            for j in d[i]:
                if not visit[j]:
                    q.append((j, counter+1))

        return 0
# Second solution (beats 5%) (Brute-force + BFS) (looping the other way around)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        s = set()
        l = len(beginWord)

        q = deque()
        q.append((beginWord, 1))

        while q:
            i, counter = q.popleft()
            s.add(i)
            if i == endWord:
                return counter
            for j in range(97, 123):
                for k in range(l):
                    tmp = i[:k]+chr(j)+i[k+1:]
                    if tmp in words and tmp not in s:
                        q.append((tmp, counter+1))

        return 0
# Third solution (beats 27%) (Brute-force + BFS) (From two ends)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        s1 = {beginWord: 1}
        s2 = {endWord: 1}
        l = len(beginWord)

        q1, q2 = deque([beginWord]), deque([endWord])

        while q1 and q2:
            if len(q1) < len(q2):
                q1, q2 = q2, q1
                s1, s2 = s2, s1
            i = q1.popleft()
            if i in s2:
                return s2[i] + s1[i] - 1
            for j in range(97, 123):
                for k in range(l):
                    tmp = i[:k]+chr(j)+i[k+1:]
                    if tmp in words and tmp not in s1:
                        s1[tmp] = s1[i] + 1
                        q1.append(tmp)

        return 0
# Fourth solution (beats 42%) (Third solution optimized chr)
from string import ascii_lowercase
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        s1 = {beginWord: 1}
        s2 = {endWord: 1}
        l = len(beginWord)

        q1, q2 = deque([beginWord]), deque([endWord])

        while q1 and q2:
            if len(q1) < len(q2):
                q1, q2 = q2, q1
                s1, s2 = s2, s1
            i = q1.popleft()
            if i in s2:
                return s2[i] + s1[i] - 1
            for k in range(l):
                for c in ascii_lowercase.replace(i[k], ''):
                    tmp = i[:k] + c + i[k+1:]
                    if tmp in words and tmp not in s1:
                        s1[tmp] = s1[i] + 1
                        q1.append(tmp)

        return 0
