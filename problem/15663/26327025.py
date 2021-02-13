import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
numbers = map(int, sys.stdin.readline().split())

for ans in sorted(set([perm for perm in itertools.permutations(numbers, M)])):
    print(*ans)