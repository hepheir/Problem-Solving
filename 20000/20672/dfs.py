import sys
import math

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{2}.in', 'r')


MOD = 10**9+7


def log(debug, state, node, ox):
    return f'{debug} -{state}-> {node}{ox}'


def modded_op(opertype, a, b, mod):
    if opertype == 0:
        # performs `(a + b) % mod`
        return (a + b) % mod
    if opertype == 1:
        # performs `(a * b) % mod`
        return ((a % mod) * (b % mod)) % mod
    raise ValueError()


def predict(node, parent, state):
    if state == 2:
        return 1
    if state == 1:
        retval = 1
        for child in graph[node]:
            if child != parent:
                retval = modded_op(state, retval, predict(child, node, 1), MOD)
                retval = modded_op(state, retval, predict(child, node, 2), MOD)
        return retval
    if state == 0:
        retval = 0
        for child in graph[node]:
            if child != parent:
                retval = modded_op(state, retval, predict(child, node, 0), MOD)
                retval = modded_op(state, retval, predict(child, node, 1), MOD)
        return retval
    raise ValueError()

def solve(node, parent=None, state=None, multiplier=None, cheatkey=None, debug=None):
    # root node
    if parent is None:
        for child in graph[node]:
            if child != parent:
                solve(child, node, 0, 1, g[node], 'root')
    # leaf node
    elif len(graph[node]) == 1:
        if node not in answer:
            answer[node] = 0
        if state == 2:
            # ends with (x)
            debug = log(debug,state,node,'x')
        else:
            # ends with (o)
            debug = log(debug,state,node,'o')
            cheatkey = math.gcd(cheatkey, g[node])
        answer[node] = modded_op(0, answer[node], multiplier * cheatkey, MOD)
        print(f'{debug}\n\tcheatkey: {cheatkey}, mult: {multiplier}\n')
    # otherwise
    else:
        predicts = dict()
        for exclude in graph[node]:
            if exclude == parent:
                continue
            for nextstate in (0, 1):
                predicts[exclude, nextstate] = 1
                for child in graph[node]:
                    if child == parent or child == exclude:
                        continue
                    predicts[exclude,nextstate] = modded_op(nextstate, predicts[exclude,nextstate], predict(child, node, nextstate), MOD)

        for child in graph[node]:
            if child != parent:
                if state == 0:
                    # (x) 0 -> 0, 2
                    solve(child, node, 0, multiplier, cheatkey, log(debug,state,node,'x'))
                    # (x) 0 -> 2, 0
                    solve(child, node, 2, modded_op(state, multiplier, predicts[child,0], MOD), cheatkey, log(debug,state,node,'x'))
                    # (o) 0 -> 1, 1
                    solve(child, node, 1, modded_op(state, multiplier, predicts[child,1], MOD), math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    # (o) 0 -> 2, 1
                    solve(child, node, 2, modded_op(state, multiplier, predicts[child,1], MOD), math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    continue
                if state == 1:
                    # (x) 1 -> 2, 2
                    solve(child, node, 2, multiplier, cheatkey, log(debug,state,node,'x'))
                    # (o) 1 -> 1, 1
                    solve(child, node, 1, modded_op(state, multiplier, predicts[child,1], MOD), math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    continue
                if state == 2:
                    # (x) 2 -> 2, 2
                    solve(child, node, 2, multiplier, cheatkey, log(debug,state,node,'x'))
                    continue


N = int(sys.stdin.readline())
g = [0, *map(int, sys.stdin.readline().split())]

graph = [list() for _ in range(N+1)]

for n in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

answer = dict()
solve(1)

print(*[answer[leaf] for leaf in sorted(answer)])
