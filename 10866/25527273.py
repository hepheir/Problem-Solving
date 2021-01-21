import collections
import sys

deque = collections.deque()

for n in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()

    if line.startswith('push_front'):
        x = int(line.split()[1])
        deque.appendleft(x)

    elif line.startswith('push_back'):
        x = int(line.split()[1])
        deque.append(x)

    elif line.startswith('pop_front'):
        print(deque.popleft() if deque else -1)

    elif line.startswith('pop_back'):
        print(deque.pop() if deque else -1)

    elif line.startswith('size'):
        print(len(deque))

    elif line.startswith('empty'):
        print(0 if deque else 1)

    elif line.startswith('front'):
        print(deque[0] if deque else -1)

    elif line.startswith('back'):
        print(deque[-1] if deque else -1)
