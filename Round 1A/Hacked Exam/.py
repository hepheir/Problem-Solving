import sys
from fractions import Fraction



def solve():
    N, Q = map(int, sys.stdin.readline().split())
    weight_t = [0] * Q
    weight_f = [0] * Q

    highest_answer = None
    highest_score = 0

    for i in range(N):
        args = sys.stdin.readline().split()
        Ai = args[0]
        Si = int(args[1])

        if Si > highest_score:
            highest_score = Si
            highest_answer = Ai

        for i, a in enumerate(Ai):
            if a == 'T':
                weight_t[i] += Si
            else:
                weight_f[i] += Si

    expected_answer = []
    expected_score = Fraction(0)
    for wt, wf in zip(weight_t, weight_f):
        if wt > wf:
            expected_answer.append('T')
            expected_score += Fraction(wt, N*Q)
        else:
            expected_answer.append('F')
            expected_score += Fraction(wf, N*Q)

    if Fraction(highest_score, 1) > expected_score:
        expected_score = Fraction(highest_score, 1)
        expected_answer = highest_answer

    y = ''.join(expected_answer)
    z = expected_score.numerator
    w = expected_score.denominator

    return y, z, w



T = int(sys.stdin.readline())
for x in range(1, T+1):
    y, z, w = solve()
    print(f'Case #{x}: {y} {z}/{w}')
