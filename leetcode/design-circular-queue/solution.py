# First solution (beats 56%)
class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None]*k
        self.head = None
        self.tail = None
        self.size = k

    def nextElement(self, index: int | None) -> int:
        if index is None:
            return 0
        if index + 1 == self.size:
            return 0
        return index + 1

    def enQueue(self, value: int) -> bool:
        if self.head is None:
            self.head = 0
            self.tail = 0
            self.data[self.head] = value
            return True
        if self.isFull():
            return False
        self.tail = self.nextElement(self.tail)
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.nextElement(self.head)
        return True

    def Front(self) -> int:
        if self.head is not None:
            return self.data[self.head]
        return -1

    def Rear(self) -> int:
        if self.tail is not None:
            return self.data[self.tail]
        return -1

    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        return False

    def isFull(self) -> bool:
        return self.head == self.nextElement(self.tail)

