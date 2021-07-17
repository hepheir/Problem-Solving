import sys
import math

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{1}.in', 'r')


def mod_mult(a, b, mod):
    # performs `(a * b) % mod`
    return ((a % mod) * (b % mod)) % mod


# DFS
def make_tree(root, graph, parent, children):
    for child in graph[root]:
        if child != parent[root]:
            parent[child] = root
            children[root].append(child)
            make_tree(child, graph, parent, children)


MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

parent = [0] * (N+1)
children = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

make_tree(1, graph, parent, children)



pass

# sys.stdout.write(' '.join([str(answer[n]) for n in sorted(answer)]))
