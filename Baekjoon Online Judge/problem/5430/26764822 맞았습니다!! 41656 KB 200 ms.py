import sys
import collections

for t in range(int(sys.stdin.readline())):
    P = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    deque = collections.deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    isReveresed = False
    if deque[0] == '':
        deque.clear()
    for p in P:
        if p == 'R':
            isReveresed = not isReveresed
        elif p == 'D':
            if not deque:
                print('error')
                break
            deque.pop() if isReveresed else deque.popleft()
    else:
        if isReveresed:
            print('['+','.join(reversed(deque))+']')
        else:
            print('['+','.join(deque)+']')
