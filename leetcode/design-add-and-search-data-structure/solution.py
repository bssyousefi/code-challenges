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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
