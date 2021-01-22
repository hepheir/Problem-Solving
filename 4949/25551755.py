from sys import stdin

stack = []
isBalanced = True

for line in stdin.read().split('.'):
    if line and line != '\n':
        stack = []
        isBalanced = True
        for c in line:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if (not stack) or (stack.pop() != '('):
                    isBalanced = False
                    break
            elif c == '[':
                stack.append(c)
            elif c == ']':
                if (not stack) or (stack.pop() != '['):
                    isBalanced = False
                    break
        isBalanced = isBalanced and (not stack)
        print('yes' if isBalanced else 'no')