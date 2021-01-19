import sys
from functools import cache

@cache
def fibonacci(x:int) -> int:
    if x == 0:
        return 1, 0
    if x == 1:
        return 0, 1
    return tuple(map(lambda x,y: x+y, fibonacci(x-1), fibonacci(x-2)))

for t in range(int(sys.stdin.readline())):
    print(*fibonacci(int(sys.stdin.readline())))