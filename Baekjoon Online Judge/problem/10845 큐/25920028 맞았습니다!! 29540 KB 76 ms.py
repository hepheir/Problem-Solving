import sys

class EmptyQueueException(BaseException):
    pass

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0

    def push(self, data) -> None:
        node = QueueNode(data)
        if self.__front is None:
            self.__front = node
        if self.__rear is not None:
            self.__rear.next = node
        self.__rear = node
        self.__size += 1

    def pop(self):
        node = self.__front
        self.__front = self.__front.next
        self.__size -= 1
        if self.empty():
            self.__rear = None
        return node.data

    def size(self) -> int:
        return self.__size
    
    def empty(self) -> bool:
        return self.__size == 0
    
    def front(self):
        return self.__front.data

    def back(self):
        return self.__rear.data

queue = Queue()

for line in sys.stdin.readlines()[1:]:
    cmd, *val = line.split()
    if cmd == 'push':
        queue.push(val[0])
    elif cmd == 'pop':
        print(queue.pop() if (not queue.empty()) else "-1")
    elif cmd == 'size':
        print(queue.size())
    elif cmd == 'empty':
        print("1" if (queue.empty()) else "0")
    elif cmd == 'front':
        print(queue.front() if (not queue.empty()) else "-1")
    elif cmd == 'back':
        print(queue.back() if (not queue.empty()) else "-1")