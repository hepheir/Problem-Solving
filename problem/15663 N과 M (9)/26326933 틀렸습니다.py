import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
numbers = list(sorted(map(int, sys.stdin.readline().split())))
answers = []
for comb in itertools.combinations(numbers, M):
    answers.append(comb)
    answers.append(comb[::-1])

for ans in sorted(set(answers)):
    print(*ans)