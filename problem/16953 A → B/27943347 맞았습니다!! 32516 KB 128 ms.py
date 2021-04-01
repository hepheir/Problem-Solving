import collections


def op1(x):
    return 2*x


def op2(x):
    return 10*x + 1


def solve():
    A, B = map(int, input().split())

    deque = collections.deque([A])
    depth = 0

    while deque:
        for w in range(len(deque)):
            x = deque.popleft()

            if (x > B): continue
            if (x == B):
                return depth+1

            deque.append(op1(x))
            deque.append(op2(x))
        depth += 1

    return '-1'


print(solve())