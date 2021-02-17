import sys

for t in range(int(sys.stdin.readline())):
    state = 0
    for c in sys.stdin.readline().rstrip():
        if c == '(':
            state += 1
        else:
            state -= 1
        if state < 0:
            break
    print('YES' if not state else 'NO')