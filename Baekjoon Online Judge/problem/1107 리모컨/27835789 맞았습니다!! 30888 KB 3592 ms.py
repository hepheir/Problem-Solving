import math
import sys


sys.setrecursionlimit(10**7)

MAX_N = 500000


def press_updown_button(src, dst):
    return abs(dst-src)


def press_number_button(buttons:list, target:int, current:int=0):
    if current != 0:
        answer = math.floor(math.log10(current)+1) + press_updown_button(current, target)
    elif (0 in buttons):
        answer = 1 + press_updown_button(current, target)
    else:
        answer = MAX_N

    if (current <= MAX_N):
        current *= 10
        for b in buttons:
            if (current == 0) and (b == 0):
                continue
            answer = min(press_number_button(buttons, target, current+b), answer)

    return answer


def solve():
    CHANNEL = 100

    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    BUTTONS = set(range(10))
    if (M > 0):
        BUTTONS -= set(map(int, sys.stdin.readline().split()))
    BUTTONS = list(BUTTONS)
    BUTTONS.sort()

    # +-로만 이동
    answer = press_updown_button(CHANNEL, N)
    answer = min(press_number_button(BUTTONS, N), answer)

    return answer

print(solve())