from sys import stdin

numbers = [*map(int,stdin.readlines()[1:])]
numbers.sort()
print('\n'.join(map(str,numbers)))