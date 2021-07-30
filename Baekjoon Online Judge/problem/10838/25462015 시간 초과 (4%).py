import sys
input = sys.stdin.readline

def get_depth(a):
    d = 0
    while a != parent[a]:
        a = parent[a]
        d += 1
    return d

def paint(a, b, c):
    da, db = map(get_depth, (a, b))
    while da > db:
        color[a] = c
        a = parent[a]
        da -= 1
    while db > da:
        color[b] = c
        b = parent[b]
        db -= 1
    while a != b:
        color[a] = c
        color[b] = c
        a = parent[a]
        b = parent[b]

def move(a, b):
    parent[a] = b

def count(a, b):
    colors = set()
    da, db = map(get_depth, (a, b))
    while da > db:
        colors.add(color[a])
        a = parent[a]
        da -= 1
    while db > da:
        colors.add(color[b])
        b = parent[b]
        db -= 1
    while a != b:
        colors.add(color[a])
        colors.add(color[b])
        a = parent[a]
        b = parent[b]
    print(len(colors))

N, K = map(int, input().split())

parent = [0]*N
color = [0]*N

for k in range(K):
    mapobj = map(int, input().split())
    r = next(mapobj)
    if r == 1:
        paint(*mapobj)
    elif r == 2:
        move(*mapobj)
    elif r == 3:
        count(*mapobj)
