# First solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _maps = []
        ret = []
        for word in strs:
            m = self.parse(word)
            if m in _maps:
                ret[_maps.index(m)].append(word)
            else:
                _maps.append(m)
                ret.append([word])
        return ret

    def parse(self, word: str):
        _map = defaultdict(int)
        for s in word:
            _map[s] += 1
        return _map

# Second solution (beats 80%)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _maps = defaultdict(list)
        ret = []
        for word in strs:
            m = self.parse(word)
            _maps[m].append(word)
        for i in _maps:
            ret.append(_maps[i])
        return ret

    def parse(self, word: str):
        return "".join(sorted(word))
