from sys import stdin

memo = dict()

stdin.readline() # not used
for x in stdin.readline().split():
    memo[x.rstrip()] = None

stdin.readline() # not used
for x in stdin.readline().split():
    print(1 if (x.rstrip() in memo) else 0)