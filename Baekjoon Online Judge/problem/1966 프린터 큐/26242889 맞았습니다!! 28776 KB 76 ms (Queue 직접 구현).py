import sys

class Queue:
    class Node:
        def __init__(self, data):
            self.next = None
            self.data = data
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def top(self):
        return self.front.data

    def enqueue(self, data):
        if self.size == 0:
            self.front = Queue.Node(data)
            self.rear = self.front
        else:
            self.rear.next = Queue.Node(data)
            self.rear = self.rear.next
        self.size += 1
    
    def dequeue(self):
        node = self.front
        self.front = self.front.next
        self.size -= 1
        return node.data

    def rotate(self):
        self.rear.next = self.front
        self.front = self.front.next
        self.rear = self.rear.next

class Data:
    def __init__(self, doc_num, priority):
        self.number = doc_num
        self.priority = priority

for t in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    answer = 0
    queue = Queue()
    stack = [] # 우선 순위 기억용
    for n, p in enumerate(map(int, sys.stdin.readline().split())):
        data = Data(n, p)
        queue.enqueue(data)
        stack.append(data.priority)
    stack.sort()
    while True:
        data = queue.top()
        if data.priority < stack[-1]:
            queue.rotate()
        elif data.number == M:
            answer += 1
            break
        else:
            stack.pop()
            queue.dequeue()
            answer += 1
    print(answer)