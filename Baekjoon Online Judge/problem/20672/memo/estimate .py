import sys


# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{1}.in', 'r')

def children(node, parent):
    for child in graph[node]:
        if child != parent:
            yield child


def estimate(node, parent, state):
    if state == -1:
        case_o = 1
        for child in children(node, parent):
            case_o *= estimate(child, node, 0) + 1
            # 각 자식은 0혹은 2의 상태를 가질 수 있으므로
            # state(0) or state(2)
            # => state(0) + state(2)
        return case_o
    if state == 0:
        case_o = 1
        case_x = 0
        for child in children(node, parent):
            case_o *= estimate(child, node, 1) + 1
            # 각 자식은 1혹은 2의 상태를 가질 수 있으므로
            # state(1) or state(2)
            # => state(1) + state(2)
            case_x += estimate(child, node, 0)
            # 한 번에 하나의 자식만 0상태, 나머지는 2이므로
            # state(0) and state(2) and state(2) and ...
            # => state(0) * state(2) * state(2) * ...
        return case_o + case_x
    if state == 1:
        case_o = 1
        for child in children(node, parent):
            case_o *= estimate(child, node, 1) + 1
            # 각 자식은 1혹은 2의 상태를 가질 수 있으므로
            # state(1) or state(2)
            # => state(1) + state(2)
        return case_o
    if state == 2:
        return 1


MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

print(estimate(1, None, -1))