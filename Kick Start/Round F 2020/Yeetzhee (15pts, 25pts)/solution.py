import sys, io
sys.stdin = io.TextIOWrapper(io.BytesIO())
sys.stdin.write('''2
3 6 2
1
2
5 2 1
5''')
sys.stdin.seek(0)

import sys
from fractions import Fraction as frac
sys.setrecursionlimit = 10**8
input = sys.stdin.readline

def solve(n_dice:int, max_num:int, n_groups:int, groups:list):
    n_dice_rolls = frac(0,1)
    n_selectable = max_num
    def roll(left:int, max_recursions=20):
        max_recursions -= 1
        if (not max_recursions) or (not left):
            return frac(1,1)
        else:
            if_succeed = frac(n_selectable, max_num) * roll(left-1, max_recursions)
            otherwise = (frac(1,1) - frac(n_selectable, max_num)) * roll(left, max_recursions)
            return if_succeed + otherwise
    for g in groups:
        n_dice_rolls += frac(1,1) + roll(g-1)
        n_selectable -= 1
    return float(n_dice_rolls)

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M, K = map(int, input().split())
        groups = []
        for k in range(K):
            groups.append(int(input()))
        ans = solve(N, M, K, groups)
        print('Case #{0}: {1:.7f}'.format(t+1, ans))