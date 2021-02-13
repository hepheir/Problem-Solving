import sys
import collections

"""
풀이 원리:
-> 각 x좌표에 대하여, 열리는 원의 갯수와 닫히는 원의 개수를 셈
"""

class Vertex():
    def __init__(self):
        self.open = 0
        self.close = 0

vertices = collections.defaultdict(Vertex)
for n in range(int(sys.stdin.readline())):
    x, r = map(int, sys.stdin.readline().split())
    vertices[x-r].open += 1
    vertices[x+r].close += 1

faces = 1 # 면의 개수
stack = [] # 원이 서로 이어져있는지 여부 저장
for x in sorted(vertices):
    vertex = vertices[x]
    for r in range(vertex.close):
        if stack.pop():
            faces += 2 # 원이 지금까지 닫혀있었으면 공간이 위 아래로 2분할
        else:
            faces += 1 # 원이 닫혀있지 않으면 공간이 연결되어 1개만 추가.
    if vertex.open:
        stack += [True]*(vertex.open-1)+[False]
    if vertex.close:
        if stack:
            stack.pop()
            stack.append(False)

print(faces)