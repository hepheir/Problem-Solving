import bisect
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack = [0] * N
size = 0
pos = [0] * N

def backtrace(idx:int, size:int):
    while idx >= 0:
        if pos[idx] == size:
            size -= 1
            yield A[idx]
        idx -= 1

if __name__ == '__main__':
    for i in range(N):
        lower_bound = bisect.bisect_left(stack, A[i], hi=size)
        stack[lower_bound] = A[i]
        pos[i] = lower_bound
        if lower_bound == size:
            size += 1

    sys.stdout.write(str(size)+'\n')
    sys.stdout.write(' '.join(map(str,reversed(tuple(backtrace(N-1, size-1))))))