import collections
import sys


class Queue:
    def __init__(self, *args):
        self.deque = collections.deque()
        self.width = 0
        self.log = [None] * 10000
        for arg in args:
            self._visit_init(arg)

    def push(self, n):
        self.width += 1
        self.deque.append(n)

    def pop(self):
        self.width -= 1
        return self.deque.popleft()

    def D(self, n):
        n *= 2
        if (n > 9999):
            n -= 10000
        return n

    def S(self, n):
        n -= 1
        if (n < 0):
            n += 10000
        return n

    def L(self, n):
        return ((n % 1000) * 10) + (n // 1000)

    def R(self, n):
        return (n % 10) * 1000 + (n // 10)

    def _visit_init(self, n):
        # 최초 방문 (초기화 용)
        self.log[n] = ''
        self.push(n)

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


class ReverseQueue(Queue):
    def D_inv(self, n):
        n //= 2
        return n

    def D_inv_ovf(self, n):
        n += 10000
        n //= 2
        return n

    def S_inv(self, n):
        n += 1
        if (n > 9999):
            n -= 10000
        return n

    def L_inv(self, n):
        return super().R(n)

    def R_inv(self, n):
        return super().L(n)

    def visit_inv(self, p, n, log):
        # p로부터 n으로 가는 연산이 log일때, 이를 방문처리하고 큐에 삽입
        if self.log[n] is not None:
            return
        self.log[n] = log + self.log[p]
        self.push(n)

    def push_DSLR_inv(self, n):
        if (n % 2 == 0):
            self.visit_inv(n, self.D_inv(n), 'D')
            self.visit_inv(n, self.D_inv_ovf(n), 'D')
        self.visit_inv(n, self.S_inv(n), 'S')
        self.visit_inv(n, self.L_inv(n), 'L')
        self.visit_inv(n, self.R_inv(n), 'R')


def solve():
    A, B = map(int, sys.stdin.readline().split())

    fq = Queue(A)  # Forward Queue
    bq = ReverseQueue(B)  # Backward Queue

    while True:
        # 같은 레벨에 위치한 모든 노드를 두 개의 큐 모두에서 탐색
        for _ in range(fq.width):
            fn = fq.pop()
            fq.push_DSLR(fn)

            if bq.log[fn] is not None:
                return fq.log[fn] + bq.log[fn]

        for _ in range(bq.width):
            bn = bq.pop()
            bq.push_DSLR_inv(bn)

            if fq.log[bn] is not None:
                return fq.log[bn] + bq.log[bn]


for t in range(int(sys.stdin.readline())):
    print(solve())
