# First solution (beats 100%) (double linked list)
class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.head = [-1, None, None]
        self.tail = [-1, None, None]
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        if self.size == 0:
            return self.insertFirstElement(value)
        node = [value, None, self.head]
        self.head[1] = node
        self.head = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        if self.size == 0:
            return self.insertFirstElement(value)
        node = [value, self.tail, None]
        self.tail[2] = node
        self.tail = node
        self.size += 1
        return True

    def insertFirstElement(self, value: int) -> bool:
        node = [value, None, None]
        self.head = self.tail = node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            return self.deleteLastElement()
        self.head = self.head[2]
        self.head[1] = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            return self.deleteLastElement()
        self.tail = self.tail[1]
        self.tail[2] = None
        self.size -= 1
        return True

    def deleteLastElement(self):
        self.head = self.tail = [-1, None, None]
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head[0]

    def getRear(self) -> int:
        return self.tail[0]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

# Second solution (beats 100%) (list)
class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.data = [-1] * k
        self.head = 0
        self.tail = k - 1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self.head = self.max_size - 1 if self.head == 0 else self.head - 1
        self.data[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self.tail = 0 if self.tail == self.max_size - 1 else self.tail + 1
        self.data[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.data[self.head] = -1
        self.head = 0 if self.head == self.max_size - 1 else self.head + 1
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.data[self.tail] = -1
        self.tail = self.max_size - 1 if self.tail == 0 else self.tail - 1
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.data[self.head]

    def getRear(self) -> int:
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
