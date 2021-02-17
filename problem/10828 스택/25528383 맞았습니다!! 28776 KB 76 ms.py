import sys

stack = []

for n in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()

    if line.startswith('push'):
        x = int(line.split()[1])
        stack.append(x)

    elif line.startswith('pop'):
        print(stack.pop() if stack else -1)

    elif line.startswith('size'):
        print(len(stack))

    elif line.startswith('empty'):
        print(1 if not stack else 0)

    elif line.startswith('top'):
        print(stack[-1] if stack else -1)
