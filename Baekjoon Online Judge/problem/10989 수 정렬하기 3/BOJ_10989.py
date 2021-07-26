from sys import stdin
from collections import Counter


def solution():
    counter = Counter()

    N = int(stdin.readline())
    for _ in range(N):
        n = int(stdin.readline())
        counter[n] += 1

    for n in sorted(counter):
        print(f'{n}\n'*counter[n], end='')


if __name__ == '__main__':
    solution()
