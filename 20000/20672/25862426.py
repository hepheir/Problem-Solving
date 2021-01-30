import sys
import math

MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]
graph = [list() for _ in range(N+1)]
level = [0]*(N+1)
parent = [n for n in range(N+1)]
children = [list() for _ in range(N+1)]
leaf = []

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [list([0,0]) for n in range(N+1)] # o 인경우, x 인경우 가능한 경우의 수


def dfs(node):
    dp[node][0] = 1
    dp[node][1] = 1
    for child in graph[node]:
        if child != parent[node]:
            parent[child] = node
            children[node].append(child)
            level[child] = level[node]+1
            dfs(child)
            dp[node][0] *= dp[child][0]+1
            dp[node][1] += sum(dp[child])-1
    if len(graph[node]) == 1 and level[node] != 0:
        leaf.append(node)


def get_path(node):
    while node != parent[node]:
        yield node
        node = parent[node]


def get_siblings(node):
    for child in children[parent[node]]:
        if child != node:
            yield child


dfs(1)

for node in sorted(leaf):
    # 경로상에 군집이 없는 경우
    cheatkey = g[1]
    count = 1
    for p in get_path(node):
        for sibling in get_siblings(p):
            count += sum(dp[sibling])-1 # 형제 노드 서브트리에 적어도 하나의 (o)가 있는 경우
    answer = cheatkey * count
    # 경로상 군집이 걸치는 깊이의 시작(i)~끝(j)
    for i in range(1, level[node]+1):  # log(n)
        for j in range(i, level[node]+1):  # log(n)
            cheatkey = g[1]
            count = 1
            camefrom = 0
            for p in get_path(node):  # log(n)
                if i <= level[p] <= j:
                    cheatkey = math.gcd(g[p], cheatkey)
                    for sibling in get_siblings(camefrom): # log(n)
                        count *= 1+dp[sibling][0]
                camefrom = p
            answer += cheatkey * count
    print(answer % MOD, end=' ')
