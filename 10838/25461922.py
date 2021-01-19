import sys
input = sys.stdin.readline

lca_cache = dict()

def depth(a):
    d = 0
    while a != 0:
        a = parent[a]
        d += 1
    return d

def lca(a, b):
    # Lowest common ancestor
    if (a,b) not in lca_cache:
        da = depth(a)
        db = depth(b)
        pa = a
        pb = b
        while da > db:
            pa = parent[pa]
            da -= 1
        while db > da:
            pb = parent[pb]
            db -= 1
        while pa != pb:
            pa = parent[pa]
            pb = parent[pb]
        lca_cache[a,b] = pa
    return lca_cache[a,b]

def paint(a, b, c):
    common_ancestor = lca(a, b)
    while a != common_ancestor:
        color[a] = c
        a = parent[a]
    while b != common_ancestor:
        color[b] = c
        b = parent[b]

def move(a, b):
    lca_cache = dict()
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
