import sys
input = sys.stdin.readline

def get_lca(a, b):
    # Lowest common ancestor
    visited = dict()
    if a == b:
        return a
    for da in range(1000):
        if not a: break
        visited[a] = True
        a = parent[a]
    for db in range(1000):
        if not b: break
        if b in visited: return b
        b = parent[b]
    return 0

def paint(a, b, c):
    lca = get_lca(a, b)
    while a != lca:
        color[a] = c
        a = parent[a]
    while b != lca:
        color[b] = c
        b = parent[b]

def move(a, b):
    parent[a] = b

def count(a, b):
    color_dict = dict()
    lca = get_lca(a, b)
    while a != lca:
        color_dict[color[a]] = None
        a = parent[a]
    while b != lca:
        color_dict[color[b]] = None
        b = parent[b]
    print(len(color_dict))

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
