import sys
while True:
    x = sys.stdin.readline().rstrip()
    if x == '0':
        break
    elif x == x[::-1]:
        print('yes')
    else:
        print('no')