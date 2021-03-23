import collections
import sys

class Queue:
    def __init__(self, *args):
        self.deque = collections.deque(args)
        self.log = [None] * 10000
        self.push = self.deque.append
        self.pop = self.deque.popleft

    def D(self, n):
        return (n << 1) % 10000

    def S(self, n):
        return 9999 if (n == 0) else n-1

    def L(self, n):
        return (n * 10 + n // 1000) % 10000

    def R(self, n):
        return (n % 10) * 1000 + (n // 10)

    def visit(self, p, n, log):
        # p로부터 n으로 가는 연산이 log일때, 이를 방문처리하고 큐에 삽입
        if self.log[n] is not None:
            return
        self.log[n] = self.log[p] + log
        self.push(n)

    def push_DSLR(self, n):
        self.visit(n, self.D(n), 'D')
        self.visit(n, self.S(n), 'S')
        self.visit(n, self.L(n), 'L')
        self.visit(n, self.R(n), 'R')


for t in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    queue = Queue(A)
    queue.log[A] = ''
    while queue:
        n = queue.pop()
        if n == B:
            print(queue.log[n])
            break
        queue.push_DSLR(n)
