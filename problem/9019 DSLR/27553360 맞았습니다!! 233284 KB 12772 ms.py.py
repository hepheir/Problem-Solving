import collections
import sys


def D(n):
    return (n << 1) % 10000

def S(n):
    return 9999 if( n == 0) else n-1

def L(n):
    return (n * 10 + n // 1000) % 10000

def R(n):
    return ((n % 10) * 1000) + (n // 10)


for t in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    visited = collections.defaultdict(lambda: False)
    deque = collections.deque([(A, '')])
    while deque:
        n, log = deque.popleft()
        if n == B:
            print(log)
            break
        if not visited[n]:
            visited[n] = True
            deque.append((D(n), log+'D'))
            deque.append((S(n), log+'S'))
            if (not log) or (log[-1] != 'R'):
                deque.append((L(n), log+'L'))
            if (not log) or (log[-1] != 'L'):
                deque.append((R(n), log+'R'))
