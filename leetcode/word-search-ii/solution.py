# First solution (Time exceeded)
class Node:
    def __init__(self, val=""):
        self.val = val
        self.neighbors = []

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        data = self.setData(board)
        ret = []
        for word in words:
            if self.search(data, word):
                ret.append(word)

        return ret

    def setData(self, board: List[List[str]]) -> List['Node']:
        b = [[None] * len(board[0]) for _ in range(len(board))]
        data = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                node = Node(board[i][j])
                if i > 0:
                    node.neighbors.append(b[i-1][j])
                    b[i-1][j].neighbors.append(node)
                if j > 0:
                    node.neighbors.append(b[i][j-1])
                    b[i][j-1].neighbors.append(node)
                b[i][j] = node
                if board[i][j] in data:
                    data[board[i][j]].append(node)
                else:
                    data[board[i][j]] = [node]
        return data

    def search(self, data, word):
        if word[0] not in data:
            return False
        visit = []
        for start in data[word[0]]:
            visit.append(start)
            if self.dfs(start, word[1:], visit):
                return True
            visit.pop()
        return False

    def dfs(self, node, word, visit=[]):
        if word == "":
            return True
        visit.append(node)
        for neighbor in node.neighbors:
            if neighbor.val == word[0] and neighbor not in visit:
                if self.dfs(neighbor, word[1:], visit):
                    return True
        visit.pop()
        return False
# Second solution (Time exceeded)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        data = self.setData()
        ret = []
        for word in words:
            if self.search(data, word):
                ret.append(word)

        return ret

    def setData(self) -> List['Node']:
        neighbors = []
        data = {}
        n = len(self.board)
        m = len(self.board[0])
        for i in range(n):
            neighbors.append([])
            for j in range(m):
                if self.board[i][j] not in data:
                    data[self.board[i][j]] = [(i,j)]
                else:
                    data[self.board[i][j]].append((i,j))
                neighbors[-1].append([])
                if i-1 > 0:
                    neighbors[-1][-1].append((i-1, j))
                if i+1 < n:
                    neighbors[-1][-1].append((i+1, j))
                if j-1 > 0:
                    neighbors[-1][-1].append((i, j-1))
                if j+1 < m:
                    neighbors[-1][-1].append((i, j+1))
        self.neighbors = neighbors
        return data

    def search(self, data, word):
        if word[0] not in data:
            return False
        visit = []
        for start in data[word[0]]:
            if self.dfs(start, word[1:], visit):
                return True
        return False

    def dfs(self, node, word, visit=[]):
        if word == "":
            return True
        visit.append(node)
        for neighbor in self.neighbors[node[0]][node[1]]:
            if self.board[neighbor[0]][neighbor[1]] == word[0] and neighbor not in visit:
                if self.dfs(neighbor, word[1:], visit):
                    return True
        visit.pop()
        return False
# Third solution (Time exceeded) (simplified solution)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        ret = []
        for word in words:
            if self.search(word):
                ret.append(word)

        return ret

    def search(self, word):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dfs(i, j, word):
                    return True
        return False

    def dfs(self, i, j, word, visit=[]):
        if word == "":
            return True
        if (i < 0 or j < 0 or 
            i == self.rows or j == self.cols or
            self.board[i][j] != word[0] or
            (i,j) in visit
        ):
            return False
        visit.append((i,j))
        ret = (
            self.dfs(i-1, j, word[1:], visit) or
            self.dfs(i+1, j, word[1:], visit) or
            self.dfs(i, j-1, word[1:], visit) or
            self.dfs(i, j+1, word[1:], visit)
        )
        visit.pop()
        return ret
# Fourth solution (beats 5%)
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.ret = set()
        trie = Trie()
        for word in words:
            trie.addWord(word)

        self.search(trie)
        return list(self.ret)

    def search(self, trie):
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, trie, "")

    def dfs(self, i, j, trie, word, visit=[]):
        if (i < 0 or j < 0 or 
            i == self.rows or j == self.cols or
            (i,j) in visit
        ):
            return False
        for c in trie.children:
            if c == self.board[i][j]:
                if trie.children[c].end:
                    self.ret.add(word+c)
                visit.append((i,j))
                self.dfs(i-1, j, trie.children[c], word+c, visit)
                self.dfs(i+1, j, trie.children[c], word+c, visit)
                self.dfs(i, j-1, trie.children[c], word+c, visit)
                self.dfs(i, j+1, trie.children[c], word+c, visit)
                visit.pop()
                break
# Final solution (beats 99.6%)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        ret = []
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
                # node = node.setdefault(c, {})
            node["#"] = word

        def dfs(i, j, trie):
            c = board[i][j]
            if c not in trie:
                return
            n = trie[c]
            if "#" in n:
                ret.append(n["#"])
                n.pop("#")

            board[i][j] = "#"

            if i > 0: dfs(i-1, j, n)
            if i < rows - 1: dfs(i+1, j, n)
            if j > 0: dfs(i, j-1, n)
            if j < cols - 1: dfs(i, j+1, n)
            board[i][j] = c
            if not n:
                trie.pop(c)

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)
        return ret
