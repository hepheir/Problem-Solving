import sys

stack = []
answer = ''
next_num = 1
for n in map(int, sys.stdin.readlines()[1:]):
    while next_num <= n:
        stack.append(next_num)
        answer += '+'
        next_num += 1
    if stack.pop() != n:
        print('NO')
        break
    else:
        answer += '-'
else:
    print('\n'.join(answer))