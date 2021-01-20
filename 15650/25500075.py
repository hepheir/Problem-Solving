from itertools import combinations

N, M = map(int, input().split())
numbers = list(range(1,N+1))

for comb in combinations(numbers, M):
    print(' '.join(map(str, comb)))