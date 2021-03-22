import collections
import sys

class ForwardQueue:
    def __init__(self, *args):
        self.deque = collections.deque(args)
        self.visited = collections.defaultdict(lambda: '')
        self.push = self.deque.append
        self.pop = self.deque.popleft

    def D(self, n):
        return (n << 1) % 10000

    def S(self, n):
        return 9999 if n == 0 else n-1

    def L(self, n):
        return (n * 10 + n // 1000) % 10000

    def R(self, n):
        return (n % 10) * 1000 + n // 10


class BackwardQueue:
    def __init__(self, *args):
        self.deque = collections.deque(args)
        self.visited = collections.defaultdict(lambda: '')
        self.push = self.deque.append
        self.pop = self.deque.popleft

    def D(self, n):  # 수행 전 짝수인지 검사해야함
        return (n >> 1)

    def S(self, n):
        return 0 if (n == 9999) else n+1

    def L(self, n):
        return (n % 10) * 1000 + n // 10

    def R(self, n):
        return (n * 10 + n // 1000) % 10000


for t in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())

    fq = ForwardQueue((A, ''))
    bq = BackwardQueue((B, ''))

    while True:
        n, log = fq.pop()
        if n == B:
            print(log)
            break
        if bq.visited[n]:
            print(log+bq.visited[n])
            break
        if not fq.visited[n]:
            fq.visited[n] = log
            fq.push((fq.D(n), log+'D'))
            fq.push((fq.S(n), log+'S'))
            fq.push((fq.L(n), log+'L'))
            fq.push((fq.R(n), log+'R'))

        n, log = bq.pop()
        if n == A:
            print(log)
            break
        if fq.visited[n]:
            print(fq.visited[n]+log)
            break
        if not bq.visited[n]:
            bq.visited[n] = log
            if n % 2 == 0:
                bq.push((bq.D(n), 'D'+log))
            bq.push((bq.S(n), 'S'+log))
            bq.push((bq.L(n), 'L'+log))
            bq.push((bq.R(n), 'R'+log))
