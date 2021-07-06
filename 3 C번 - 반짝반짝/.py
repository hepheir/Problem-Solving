import sys
import itertools
import functools

DIR = 'contest/587 2021 신촌지역 대학생 프로그래밍 대회 동아리 연합 겨울 대회 (SUAPC 2021 Winter) Open/3 C번 - 반짝반짝/data/boj/sample/'
sys.stdin = open(DIR+'1'+'.in', 'r')

N, K = map(int, sys.stdin.readline().split())
P = list(map(float, sys.stdin.readline().split()))

@functools.cache
def p(start, end) -> float: # 전구가 start부터 end까지 모두 들어올 확률
    if start < end:
        return p(start, end-1) * (1-P[end])
    else:
        return 1-P[start]

def E(start, end): # start부터 end전 까지 불이 켜질 전구의 수의 기댓값
    retval = 0
    for e in range(start, end+1):
        retval += (e-start+1) * p(start, e)
    return retval


answer = 0
for comb in itertools.combinations(range(1, N-1), K-1):
    comb = list(comb)+[N]
    expectation = 0
    start = 0
    for end in comb:
        expectation += E(start, end)
        start = end
    answer = max(expectation, answer)
print(answer)