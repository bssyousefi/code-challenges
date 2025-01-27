# First solution (beats 36%)
class WordDictionary:

    def __init__(self):
        self.data = {"children":{}, "end": True}


    def addWord(self, word: str) -> None:
        node = self.data
        for c in word:
            if c not in node["children"]:
                node["children"][c] = {"children":{}, "end": False}
            node = node["children"][c]
        node["end"] = True


    def search(self, word: str) -> bool:
        return self.searchChar(word, self.data)


    def searchChar(self, word: str, node: dict) -> bool:
        if word == "":
            if node["end"]:
                return True
            else:
                return False
        if word[0] != ".":
            if word[0] in node["children"]:
                return self.searchChar(word[1:], node["children"][word[0]])
            else:
                return False
        else:
            for child in node["children"]:
                ret = self.searchChar(word[1:], node["children"][child])
                if ret:
                    return True
            return False
# Second solution (beats 91%) (same solution)
class WordDictionary:

    def __init__(self):
        self.data = {}

    def addWord(self, word):
        self.add(word, self.data)

    def add(self, word, data):
        if len(word) == 0:
            data["#"] = True
            return

        if word[0] not in data:
            data[word[0]] = {}
        self.add(word[1:], data[word[0]])

    def search(self, word):
        return self.get(word, self.data)

    def get(self, word, data):
        if len(word) == 0:
            return True if "#" in data else False
        if word[0] == ".":
            for child in data:
                if child != "#" and self.get(word[1:],data[child]):
                    return True
            return False
        else:
            if word[0] not in data:
                return False
            return self.get(word[1:], data[word[0]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
