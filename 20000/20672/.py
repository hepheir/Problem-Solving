import sys
import math
import collections

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{2}.in', 'r')

def children(node, parent):
    for child in graph[node]:
        if child != parent:
            yield child


def siblings(node, parent, child):
    for sibling in children(node, parent):
        if sibling != child:
            yield sibling


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


def update_cheatkey(node, cheatkey):
    return math.gcd(cheatkey, g[node])


def update_multiverses(isActiveNode, multiverses, node, parent, child):
    if isActiveNode:
        for sibling in siblings(node, parent, child):
            multiverses *= estimate(sibling, node, 1) + estimate(sibling, node, 2)
    else:
        multiverses *= sum(estimate(sibling, node, 0) for sibling in siblings(node, parent, child))
    return multiverses


def is_leaf(node, parent):
    # return not len(children(node, parent)) # TypeError: object of type 'generator' has no len()
    return (parent) and (len(graph[node]) == 1)


def update_log(node, log=tuple()):
    return log+(g[node],)


def solve(node, parent, state, cheatkey, multiverses, log=tuple()):
    if is_leaf(node, parent):
        if state != 2:
            cheatkey = update_cheatkey(node, cheatkey)
            log = update_log(node, log)
        answer[node] += cheatkey * multiverses
        print(f'e:{node:<2d} c:{cheatkey:<10d} m:{multiverses:<4d} {str(log)}')
        return
    if state == -1:
        # (o)
        for child in children(node, parent):
            solve(child, node, 0, g[node], 1, update_log(node))
            solve(child, node, 2, g[node], 1, update_log(node))
        return
    if state == 0:
        # (x)
        for child in children(node, parent):
            solve(child, node, 0, cheatkey, multiverses, log) # all the others should be 2 state
            solve(child, node, 2, cheatkey, update_multiverses(False, multiverses, node, parent, child), log) # one of the others can be 0 state
        # (o)
        cheatkey = update_cheatkey(node, cheatkey)
        for child in children(node, parent):
            solve(child, node, 1, cheatkey, update_multiverses(True, multiverses, node, parent, child), update_log(node, log))
            solve(child, node, 2, cheatkey, update_multiverses(True, multiverses, node, parent, child), update_log(node, log))
        return
    if state == 1:
        # (x)
        for child in children(node, parent):
            solve(child, node, 2, cheatkey, multiverses, log)
        # (o)
        cheatkey = update_cheatkey(node, cheatkey)
        for child in children(node, parent):
            solve(child, node, 1, cheatkey, update_multiverses(True, multiverses, node, parent, child), update_log(node, log))
        return
    if state == 2:
        # (x)
        for child in children(node, parent):
            solve(child, node, 2, cheatkey, multiverses, log)
        return


MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


answer = collections.defaultdict(lambda: 0)

solve(1, 0, -1, 0, 0)
# dfs start node: 1 (root node)
# parent: 0 (no parent)
# state: -1 (initial value, indicates root)
# cheatkey: 0 (initial value)
# multiverses: 0 (initial value)


print(*(answer[node]%MOD for node in sorted(answer)))

pass