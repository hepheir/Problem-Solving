import sys
input = sys.stdin.readline

def depth(a):
    d = 0
    while a != 0:
        a = parent[a]
        d += 1
    return d

def lca(a, b):
    # Lowest common ancestor
    da = depth(a)
    db = depth(b)
    while da > db:
        a = parent[a]
        da -= 1
    while db > da:
        b = parent[b]
        db -= 1
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

def paint(a, b, c):
    common_ancestor = lca(a, b)
    while a != common_ancestor:
        color[a] = c
        a = parent[a]
    while b != common_ancestor:
        color[b] = c
        b = parent[b]

def move(a, b):
    parent[a] = b

def count(a, b):
    colors = dict()
    common_ancestor = lca(a, b)
    while a != common_ancestor:
        if color[a] not in colors:
            colors[color[a]] = True
        a = parent[a]
    while b != common_ancestor:
        if color[b] not in colors:
            colors[color[b]] = True
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
