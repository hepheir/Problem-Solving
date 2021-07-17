from sys import stdin

numbers = dict()

N = int(stdin.readline())
for n in range(N):
    x = int(stdin.readline())
    if x not in numbers:
        numbers[x] = 0
    numbers[x] += 1
for x in sorted(numbers):
    print('\n'.join([str(x)]*numbers[x]))