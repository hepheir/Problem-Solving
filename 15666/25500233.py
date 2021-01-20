from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = sorted(set(input().split()))

print('\n'.join(map(' '.join, combinations_with_replacement(numbers, M))))