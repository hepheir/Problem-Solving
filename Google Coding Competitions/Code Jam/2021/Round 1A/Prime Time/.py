import bisect
import sys
import collections


def counter_sum(counter):
    retval = 0
    for num, cnt in counter.items():
        retval += num * cnt
    return retval

def counter_mul(counter):
    retval = 1
    for num, cnt in counter.items():
        retval *= num ** cnt
    return retval


def solve():
    M = int(sys.stdin.readline())

    COUNTER = collections.Counter()
    deque = collections.deque()
    numbers = []
    sum_of_all = 0

    for _ in range(M):
        p, n = map(int, sys.stdin.readline().split())
        COUNTER[p] = n
        numbers.append(p)

        sum_of_all += p * n

        node = collections.Counter()
        node[p] = 1
        deque.append(node)

    numbers.sort()

    maxsum = 0

    while deque:
        counter = deque.popleft()

        sum_group = sum_of_all - counter_sum(counter)
        mul_group = counter_mul(counter)

        if sum_group == mul_group:
            maxsum = max(sum_group, maxsum)

        if mul_group < sum_of_all:
            for x in numbers[bisect.bisect_left(numbers, max(counter)):]:
                if counter[x] < COUNTER[x]:
                    node = counter.copy()
                    node[x] += 1
                    deque.append(node)
    return maxsum


T = int(sys.stdin.readline())
for t in range(1, T+1):
    print('Case #{x}: {y}'.format(x=t, y=solve()))
