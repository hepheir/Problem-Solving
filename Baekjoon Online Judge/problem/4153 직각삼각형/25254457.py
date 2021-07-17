import sys

while True:
    a, b, c = sorted(map(int, sys.stdin.readline().rstrip().split()))
    if a == b == c == 0:
        break
    elif (c**2) == (a**2 + b**2):
        print('right')
    else:
        print('wrong')