from sys import stdin

for line in stdin.readlines():
    line = line.rstrip()
    if line == '.':
        break
    stack = []
    isBalanced = True
    for c in line:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if (not stack) or (stack.pop() != '('):
                isBalanced = False
                break
        elif c == '[':
            stack.append('[')
        elif c == ']':
            if (not stack) or (stack.pop() != '['):
                isBalanced = False
                break
    print('yes' if isBalanced else 'no')