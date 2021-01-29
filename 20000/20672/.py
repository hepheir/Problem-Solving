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


def case_x_multiverses(node, parent, child, multiverses):
    # only one of the sibling is 0, the others are 2
    retval = 0
    for sibling in siblings(node, parent, child):
        retval += estimate(sibling, node, 0)
    return retval * multiverses


def case_o_multiverses(node, parent, child, multiverses):
    # all siblings can be both 1 or 2
    retval = 1
    for sibling in siblings(node, parent, child):
        retval *= estimate(sibling, node, 1) + estimate(sibling, node, 2)
    return retval * multiverses


def is_leaf(node, parent):
    # return not len(children(node, parent)) # TypeError: object of type 'generator' has no len()
    return (parent) and (len(graph[node]) == 1)


def update_log(node, state, log=tuple()):
    genom = None
    if node is not None:
        genom = g[node]
    return log+((genom, state),)


def solve(node, parent, state, cheatkey, multiverses, log=tuple()):
    if is_leaf(node, parent):
        if  state != 2:
            # (o)
            cheatkey = update_cheatkey(node, cheatkey)
            log = update_log(node, state, log)
        answer[node] += cheatkey * multiverses
        statistic.append((node, cheatkey, multiverses, log))
        return
    if state == -1:
        # (o)
        cheatkey = g[node]
        multiverses = 1
        for child in children(node, parent):
            solve(child, node, 0, cheatkey, multiverses, update_log(node, state, log))
            solve(child, node, 2, cheatkey, multiverses, update_log(node, state, log))
        return
    if state == 0:
        # (x)
        for child in children(node, parent):
            solve(child, node, 0, cheatkey, multiverses, update_log(0, state, log)) # all the others should be 2 state
            solve(child, node, 2, cheatkey, multiverses, update_log(0, state, log)) # all the others are 2
            solve(child, node, 2, cheatkey, case_x_multiverses(node, parent, child, multiverses), update_log(0, state, log)) # one of the others can be 0 state
        # (o)
        cheatkey = update_cheatkey(node, cheatkey)
        for child in children(node, parent):
            solve(child, node, 1, cheatkey, case_o_multiverses(node, parent, child, multiverses), update_log(node, state, log))
            solve(child, node, 2, cheatkey, case_o_multiverses(node, parent, child, multiverses), update_log(node, state, log))
        return
    if state == 1:
        # (x)
        for child in children(node, parent):
            solve(child, node, 2, cheatkey, multiverses, update_log(0, state, log))
        # (o)
        cheatkey = update_cheatkey(node, cheatkey)
        for child in children(node, parent):
            solve(child, node, 1, cheatkey, case_o_multiverses(node, parent, child, multiverses), update_log(node, state, log))
        return
    if state == 2:
        # (x)
        for child in children(node, parent):
            solve(child, node, 2, cheatkey, multiverses, update_log(0, state, log))
        return


MOD = 10**9+7

N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


statistic = []
answer = collections.defaultdict(lambda: 0)

solve(1, 0, -1, 0, 0)
# dfs start node: 1 (root node)
# parent: 0 (no parent)
# state: -1 (initial value, indicates root)
# cheatkey: 0 (initial value)
# multiverses: 0 (initial value)

statistic.sort()
for node, cheatkey, multiverses, log in statistic:
    print(f'e:{node:<2d} c:{cheatkey:<10d} m:{multiverses:<4d} ', end='')
    for g, state in log:
        if not g:
            g = 'x'
        print(f' -[{state}]-> {g}', end='')
    print()
        

print(*(answer[node]%MOD for node in sorted(answer)))

pass