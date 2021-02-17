from itertools import permutations

N, M = map(int, input().split())
numbers = list(sorted(set(map(int, input().split()))))

for perm in permutations(numbers, M):
    print(' '.join(map(str, perm)))