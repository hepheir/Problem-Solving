import sys

stack = []
answer = ''
next_num = 1

def push():
    global stack, answer, next_num
    stack.append(next_num)
    answer += '+'
    next_num += 1

def pop():
    global stack, answer, next_num
    stack.pop()
    answer += '-'

try:
    for n in map(int, sys.stdin.readlines()[1:]):
        if next_num == n:
            push()
            pop()
        elif next_num < n:
            while next_num <= n:
                push()
            pop()
        elif stack[-1] == n:
            pop()
        else:
            raise Exception
    print('\n'.join(answer))
except:
    print('NO')