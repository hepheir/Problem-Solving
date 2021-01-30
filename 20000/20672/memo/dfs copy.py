import sys
import math

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{1}.in', 'r')


MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (N+1)
cases = []
leafs = set()

def mod_mult(a, b, mod):
    # performs `(a * b) % mod`
    return ((a % mod) * (b % mod)) % mod


def dfs(node, state=-1, logs=None):
    # Leaf node
    if (state != -1) and (len(graph[node]) == 1):
        if state != 2:
            logs+=(node,)
        cases.append(logs)
        leafs.add(node)
    else:
        for child in graph[node]:
            if child != parent[node]:
                parent[child] = node
                # Root node
                if state == -1:
                    dfs(child, 0, (node,))
                # No biome yet
                elif state == 0:
                    # (x)
                    dfs(child, 0, logs)
                    dfs(child, 2, logs)
                    # (o)
                    dfs(child, 1, logs+(node,))
                # Connected to biome
                elif state == 1:
                    # (x)
                    dfs(child, 2, logs)
                    # (o)
                    dfs(child, 1, logs+(node,))
                # Disconnected from biome
                else: # state == 2
                    # (x)
                    dfs(child, 2, logs)
    return logs

dfs(1)

pass

# sys.stdout.write(' '.join([str(answer[n]) for n in sorted(answer)]))