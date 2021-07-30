from sys import stdin

stack = []
for x in map(int, stdin.readlines()[1:]):
    if not x:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))