import sys
import bisect


class Ticks(int):
    pass

H_HAND_TICKS_PER_NS = 1
M_HAND_TICKS_PER_NS = 12
S_HAND_TICKS_PER_NS = 720


TICKS_PER_CYCLE = 360 * 12 * int(1e10)
TICKS_PER_H = TICKS_PER_CYCLE // 12
TICKS_PER_M = TICKS_PER_CYCLE // 60
TICKS_PER_S = TICKS_PER_M


NS_PER_S = int(1e9)
NS_PER_M = 60 * NS_PER_S
NS_PER_H = 60 * NS_PER_M


def rotate_clockwise(r:Ticks, a:Ticks, b:Ticks, c:Ticks):
    return map(lambda x: ((x+r) % TICKS_PER_CYCLE), (a, b, c))


def hourMin_sync(h:Ticks, m:Ticks):
    h %= TICKS_PER_H
    h //= H_HAND_TICKS_PER_NS
    m //= M_HAND_TICKS_PER_NS
    return h == m


def minSec_sync(m:Ticks, s:Ticks):
    m %= TICKS_PER_M
    m //= M_HAND_TICKS_PER_NS
    s //= S_HAND_TICKS_PER_NS
    return m == s


def findHMS(a:Ticks, b:Ticks, c:Ticks):
    if hourMin_sync(a, b) and minSec_sync(b, c):
        h, m, s = a, b, c
    elif hourMin_sync(a, c) and minSec_sync(c, b):
        h, m, s = a, c, b
    elif hourMin_sync(b, a) and minSec_sync(a, c):
        h, m, s = b, a, c
    elif hourMin_sync(b, c) and minSec_sync(c, a):
        h, m, s = b, c, a
    elif hourMin_sync(c, a) and minSec_sync(a, b):
        h, m, s = c, a, b
    elif hourMin_sync(c, b) and minSec_sync(b, a):
        h, m, s = c, b, a
    else:
        raise ValueError()
    return (h // TICKS_PER_H), (m // TICKS_PER_M), (s // TICKS_PER_S), (S_HAND_TICKS_PER_NS - s % TICKS_PER_S)



def solve():
    A, B, C = map(int, sys.stdin.readline().split())
    h, m, s, ns = 0, 0, 0, 0

    rotate_tick = 0

    while rotate_tick < TICKS_PER_CYCLE:
        while math.gcd(A, B, C) == 1:
            rotate_tick += 1
        a, b, c = rotate_clockwise(rotate_tick, A, B, C)
        try:
            h, m, s, ns = findHMS(a, b, c)
            return h, m, s, ns
        except ValueError:
            continue

    return h, m, s, ns


T = int(sys.stdin.readline())
for x in range(1, T+1):
    h, m, s, n = solve()
    print(f'Case #{x}: {h} {m} {s} {n}')