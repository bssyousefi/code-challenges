# First solution (beats 93%) (based on lru-cache implementation in CPython)
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            pre = self.cache[key][0]
            nex = self.cache[key][1]
            pre[1] = nex
            nex[0] = pre
            self.cache[key][1] = self.root[1]
            self.cache[key][0] = self.root
            self.root[1][0] = self.cache[key]
            self.root[1] = self.cache[key]
            return self.cache[key][3]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            pre = self.cache[key][0]
            nex = self.cache[key][1]
            pre[1] = nex
            nex[0] = pre
            self.cache[key][1] = self.root[1]
            self.cache[key][0] = self.root
            self.root[1][0] = self.cache[key]
            self.root[1] = self.cache[key]
            self.cache[key][3] = value
        else:
            if len(self.cache) == self.cap:
                oldkey = self.root[0][2]
                self.cache.pop(oldkey)
                self.root[0][0][1] = self.root
                self.root[0] = self.root[0][0]
            node = [self.root, self.root[1], key, value]
            self.root[1][0] = node
            self.root[1] = node
            self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
