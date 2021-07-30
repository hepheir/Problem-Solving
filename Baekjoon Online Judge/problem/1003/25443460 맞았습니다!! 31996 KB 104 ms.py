from sys import stdin
from functools import cache
from operator import add

@cache
def fibonacci(x:int) -> int:
    """ returns a tuple of (fibo_0_count, fibo_1_count, fibo_n)"""
    if x == 0:
        return 1, 0, 0
    if x == 1:
        return 0, 1, 1
    return tuple(map(add, fibonacci(x-1), fibonacci(x-2)))

for t in range(int(stdin.readline())):
    cnt0, cnt1, fibo = fibonacci(int(stdin.readline()))
    print(cnt0, cnt1)