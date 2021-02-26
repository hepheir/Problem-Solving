import sys
import collections

for t in range(int(sys.stdin.readline())):
    P = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    inner_deque = sys.stdin.readline().rstrip()[1:-1]
    DEQUE = collections.deque(inner_deque.split(',') if inner_deque else [])
    for p in P:
        if p == 'R':
            DEQUE.reverse()
        elif p == 'D':
            try:
                DEQUE.popleft()
            except IndexError:
                print('error')
                break
    else:
        print('['+','.join(DEQUE)+']')

