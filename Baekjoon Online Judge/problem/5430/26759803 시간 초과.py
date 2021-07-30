import sys

for t in range(int(sys.stdin.readline())):
    P = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline())
    ARR = eval(sys.stdin.readline())
    for p in P:
        if p == 'R':
            ARR.reverse()
        elif p == 'D':
            if ARR:
                ARR.pop(0)
            else:
                print('error')
                break
    else:
        print(str(ARR).replace(' ',''))