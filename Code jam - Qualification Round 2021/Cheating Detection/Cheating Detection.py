import math
import sys


CORRECT = 1
INCORRECT = 0

STUDENTS = 100
QUESTIONS = 10000

def f(x): # Sigmoid
    return 1/(1+math.exp(-x))


def make_uniform(array):
    return (3 - 6 * (sum(array) / len(array)))


def solve():
    OMR = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(STUDENTS)]
    S = [make_uniform(OMR[s]) for s in range(STUDENTS)]
    Q = [make_uniform([OMR[s][q] for s in range(STUDENTS)]) for q in range(QUESTIONS)]
    ERROR = [[(OMR[s][q] - f(S[s]-Q[q])) for q in range(QUESTIONS)] for s in range(STUDENTS)]
    ERROR_STUDENT = [sum(ERROR[s]) for s in range(STUDENTS)]

    answer = 0
    max_error = ERROR_STUDENT[0]
    for s in range(STUDENTS):
        if ERROR_STUDENT[s] > max_error:
            answer = s
            max_error = ERROR_STUDENT[s]

    return answer+1

T = int(sys.stdin.readline())
P = int(sys.stdin.readline())
for t in range(1, T+1):
    print(f'Case #{t}: {solve()}')