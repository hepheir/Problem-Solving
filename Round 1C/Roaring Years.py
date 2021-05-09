import sys
import math


def slice_int(integer, start, end):
    digits = math.log10(integer)
    retval = 0
    while start < end:
        retval *= 10
        retval += integer // 10 ** start
        start += 1
        integer %= 10 ** digits
        digits -= 1


def roaring(prev:int, next:int):
    if math.log10(prev) > math.log10(next):
        return -1

    roaring()


def solve():
    Y = list(map(int, sys.stdin.readline()))



T = int(sys.stdin.readline())
for x in range(1, T+1):
    print("Case #{x}: {z}".format(x=x, z=solve()))