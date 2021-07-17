#!/usr/bin/python3.8

import sys
import math
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    edges = [] # 간선
    connects = [0]*N # 정점에 연결된 간선의 수
    for n in range(N-1):
        u, v = map(lambda x: int(x)-1, input().split())
        edges.append((u,v))
        connects[u] += 1
        connects[v] += 1
    D = 0
    G = 0
    for u, v in edges:
        D += (connects[u]-1) * (connects[v]-1)
    for n in range(N):
        G += math.comb(connects[n],3)
    if D == G*3:
        print('DUDUDUNGA')
    elif D > G*3:
        print('D')
    else:
        print('G')