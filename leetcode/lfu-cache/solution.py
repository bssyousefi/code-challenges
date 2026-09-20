# First solution (beats 72%) (doubly linked list + hashmap)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.freqs = defaultdict(self.new_freq)
        self.size = 0
        self.min_freq = None

    @staticmethod
    def new_freq():
        head = [None, None, None, None, None] # key, value, freq, prev, next
        tail = [None, None, None, None, None]
        head[4], tail[3] = tail, head
        return [0, head, tail]

    def pop(self, node):
        node[3][4], node[4][3] = node[4], node[3]
        self.freqs[node[2]][0] -= 1
        if self.freqs[node[2]][0] == 0 and self.min_freq == node[2]:
            self.min_freq += 1
        self.size -= 1
    
    def insert(self, node):
        head = self.freqs[node[2]][1]
        tail = self.freqs[node[2]][2]
        node[3], node[4] = head, head[4]
        head[4][3], head[4] = node, node
        self.freqs[node[2]][0] += 1
        if self.min_freq is None or node[2] < self.min_freq:
            self.min_freq = node[2]

        self.size += 1
    
    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node = self.data[key]
        self.pop(node)
        node[2] += 1
        self.insert(node)
        return node[1]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key][1] = value
            self.get(key)
            return
        
        if self.size == self.capacity:
            node = self.freqs[self.min_freq][2][3]
            self.pop(node)
            del self.data[node[0]]
        new_node = [key, value, 1, None, None]
        self.insert(new_node)
        self.data[key] = new_node
       

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
