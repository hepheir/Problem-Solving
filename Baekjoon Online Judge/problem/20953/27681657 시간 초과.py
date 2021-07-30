import sys

def dolmen(a:int, b:int):
    sum = 0
    for i in range(a+b):
        for j in range(a+b):
            for k in range(j):
                sum += 1
    return sum

T = int(sys.stdin.readline())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(dolmen(a, b))