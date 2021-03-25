import sys


def dolmen(a:int, b:int):
    # sum = 0
    # for i in range(a+b):
    #     for j in range(a+b):
    #         for k in range(j):
    #             sum += 1
    # return sum
    
    # for i in range(a+b):
    #     for j in range(a+b):
    #         sum += j

    # 등차수열의 합
    n = a+b-1
    return (a+b)*(n*(n+1)//2)


T = int(sys.stdin.readline())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(dolmen(a, b))