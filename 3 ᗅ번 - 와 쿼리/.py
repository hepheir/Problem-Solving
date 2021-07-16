import sys


def solve():
    Q = int(sys.stdin.readline())

    for q in range(Q):
        x = sys.stdin.readline().rstrip()
        if x == '1':
            print('업데이트')
        elif x == '2':
            print('출력')