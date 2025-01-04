# First solution (beats 17%)
class Trie:

    def __init__(self):
        self.map = {}


    def insert(self, word: str) -> None:
        if word == "":
            self.map[word] = None
            return
        if word[0] not in self.map:
            self.map[word[0]] = Trie()

        self.map[word[0]].insert(word[1:])


    def search(self, word: str) -> bool:
        if word == "":
            if word in self.map:
                return True
            else:
                return False
        if word[0] not in self.map:
            return False

        return self.map[word[0]].search(word[1:])


    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        if prefix[0] not in self.map:
            return False
        return self.map[prefix[0]].startsWith(prefix[1:])


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Second solution (beats 88%)
class Trie:

    def __init__(self):
        self.map = {"":{}}


    def insert(self, word: str) -> None:
        node = self.map
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[""] = {}


    def search(self, word: str) -> bool:
        if word == "":
            return True
        node = self.map
        for c in word:
            if c not in node:
                return False
            node = node[c]
        if "" not in node:
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        node = self.map
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
