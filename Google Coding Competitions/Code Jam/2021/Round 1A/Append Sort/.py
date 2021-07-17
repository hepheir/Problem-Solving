import sys
import math


def digit_length(x):
    if x == 0:
        return 1
    return math.floor(math.log10(x)) + 1


def solve():
    N = int(sys.stdin.readline())
    answer = 0
    last_num = 0
    for x in map(int, sys.stdin.readline().split()):
        x_increased = x
        x_shifted_count = 0
        while digit_length(last_num) > digit_length(x_increased):
            x_increased *= 10
            x_shifted_count += 1

        x_samedigit_max = x_increased
        for shift in range(x_shifted_count):
            x_samedigit_max += 9 * (10**shift)

        if last_num >= x_samedigit_max:
            x_increased *= 10
        elif last_num >= x_increased:
            x_increased = last_num + 1

        answer += digit_length(x_increased) - digit_length(x)
        last_num = x_increased
    return answer



T = int(sys.stdin.readline())
for t in range(1, T+1):
    print('Case #{x}: {y}'.format(x=t, y=solve()))
