import sys
import math

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{1}.in', 'r')


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

def solve(node, parent=None, state=-1, othercases=0, cheatkey=1, debug=''):
    # leaf node
    if (parent is not None) and (len(graph[node]) == 1):
        if node not in answer:
            answer[node] = 0
        if state == 2:
            # ends with (x)
            debug = log(debug,state,node,'x')
        else:
            # ends with (o)
            cheatkey = math.gcd(cheatkey, g[node])
            debug = log(debug,state,node,'o')
        print(f'{debug}\n\tcheatkey: {cheatkey}, alts: {othercases}\n')
        answer[node] += cheatkey * (1+othercases)
        answer[node] %= MOD
    # otherwise
    else:
        predicts = dict()
        for exclude in graph[node]:
            if exclude == parent:
                continue
            predicts[exclude, 0] = 0
            predicts[exclude, 1] = 1
            for child in graph[node]:
                if child == parent or child == exclude:
                    continue
                predicts[exclude,0] = predicts[exclude,0] + predict(child,node,0)
                predicts[exclude,1] = (predicts[exclude,1] % MOD) * (predict(child,node,1) % MOD) % MOD

        for child in graph[node]:
            if child != parent:
                if state == -1:
                    # (o) -1 -> 0
                    solve(child, node, 0, 0, g[node], 'root')
                    # (o) -1 -> 2
                    solve(child, node, 2, 0, g[node], 'root')
                if state == 0:
                    # (x) 0 -> 0, 2
                    solve(child, node, 0, othercases, cheatkey, log(debug,state,node,'x'))
                    # (x) 0 -> 2, 0
                    solve(child, node, 2, othercases+predicts[child,0], cheatkey, log(debug,state,node,'x'))
                    # (o) 0 -> 1, 1
                    solve(child, node, 1, othercases+predicts[child,1], math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    # (o) 0 -> 2, 1
                    solve(child, node, 2, othercases+predicts[child,1], math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    continue
                if state == 1:
                    # (x) 1 -> 2, 2
                    solve(child, node, 2, othercases, cheatkey, log(debug,state,node,'x'))
                    # (o) 1 -> 1, 1
                    solve(child, node, 1, othercases+predicts[child,1], math.gcd(cheatkey, g[node]), log(debug,state,node,'o'))
                    continue
                if state == 2:
                    # (x) 2 -> 2, 2
                    solve(child, node, 2, othercases, cheatkey, log(debug,state,node,'x'))
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

print(answer)
print(*[answer[leaf] for leaf in sorted(answer)])