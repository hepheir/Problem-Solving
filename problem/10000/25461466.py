import sys

vertices = dict() # {X:(LEFT_CNT, RIGHT_CNT)}
for n in range(int(sys.stdin.readline())):
    x, r = map(int, sys.stdin.readline().split())
    left, right = x-r, x+r
    if left not in vertices:
        vertices[left] = [0, 0]
    if right not in vertices:
        vertices[right] = [0, 0]
    vertices[left][0] += 1
    vertices[right][1] += 1

faces = 1
stack = []
for x in sorted(vertices):
    left, right = vertices[x]
    for r in range(right):
        if stack.pop() == 1:
            faces += 2
        else:
            faces += 1
    if left:
        stack += [1]*(left-1)+[0]
    elif stack:
        stack.pop()
        stack.append(-1)

print(faces)