import sys
import itertools

from fractions import Fraction

import collections


HALF = Fraction(1, 2)

def solve():
    N, Q = map(int, sys.stdin.readline().split())

    count_t = [0] * Q
    total_cases = 0

    for i in range(N):
        args = sys.stdin.readline().split()
        Ai = list(args[0])
        Si = int(args[1])

        deque = collections.deque((Ai, Si))

        while deque:
            a, s = deque.popleft()

            if not s:
                for idx, char in a:
                    if char == 'T':
                        count_t[idx] += 1
                total_cases += 1
            else:



        for comb in itertools.combinations(range(Q), Si):
            for c in comb:

                if Ai[c] == 'T':
                    count_t[c] += 1
            total_cases += 1

    expected_answer = []
    expected_score = Fraction(0)

    for cnt in count_t:
        p = Fraction(cnt, total_cases)
        if p > HALF:
            expected_answer.append('T')
            expected_score += p
        else:
            expected_answer.append('F')
            expected_score += (p + -1) * -1

    y = ''.join(expected_answer)
    z = expected_score.numerator
    w = expected_score.denominator

    return y, z, w



T = int(sys.stdin.readline())
for x in range(1, T+1):
    y, z, w = solve()
    print(f'Case #{x}: {y} {z}/{w}')
