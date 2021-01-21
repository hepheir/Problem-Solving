import collections
import sys

queue = collections.deque()

for n in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()

    if line.startswith('push'):
        x = int(line.split()[1])
        queue.append(x)

    elif line.startswith('pop'):
        print(queue.popleft() if queue else -1)

    elif line.startswith('size'):
        print(len(queue))

    elif line.startswith('empty'):
        print(1 if not queue else 0)

    elif line.startswith('front'):
        print(queue[0] if queue else -1)

    elif line.startswith('back'):
        print(queue[-1] if queue else -1)
