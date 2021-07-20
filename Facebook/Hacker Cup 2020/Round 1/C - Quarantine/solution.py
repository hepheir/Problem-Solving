import sys
import functools

file_name = 'Round 1/C - Quarantine/data/sample_input.txt'

if __name__ == '__main__'
    sys.stdin = open(file_name, 'r')
    sys.stdout = open(file_name.replace('input','output'), 'w')
    input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    S = input()
    E = list(map(int, input().split()))
    A,B,C = map(int, input().split())
    for i in range(K,N):
        E.append(((A*E[i-2]+B*E[i-1]+C) % (i-1))+1)
    connects = dict()
    for i in range(N):
        if S[i] == '*':
            connects[i] = []



if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        answer = solve(t)
        print(f'Case #{t}: {answer}')