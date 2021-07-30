import sys
sys.setrecursionlimit(10**6)

def allocation(N):
    global connect
    global subtree_size
    connect = [[] for n in range(N+1)]
    subtree_size = [0] * (N+1)

def connect_node(u, v):
    connect[u].append(v)
    connect[v].append(u)


def count_subtree_size(root):
    subtree_size[root] = 1
    for node in connect[root]:
        if not subtree_size[node]:
            count_subtree_size(node)
            subtree_size[root] += subtree_size[node]

def testcase():
    N, R, Q = map(int, sys.stdin.readline().split())

    allocation(N)

    for n in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        connect_node(u, v)

    count_subtree_size(R)

    for u in (map(int, sys.stdin.readlines())):
        print(subtree_size[u])

if __name__ == '__main__':
    testcase()