import sys

MOD = 1000000007

N, M, K = map(int, sys.stdin.readline().split())

tree = [None]+[1]*(4*N)
array = [None] # dummy for 1-base indexing

def mod_mult(x, y, mod):
    # 나머지 연산의 분배 법칙 이용
    return (x % mod) * (y % mod) % mod

def make(start, end, node):
    if start == end:
        tree[node] = array[start]
    else:
        mid = (start+end)//2
        tree[node] = mod_mult(make(start, mid, node*2), make(mid+1, end, node*2+1), MOD)
    return tree[node]

def update(start, end, node, index, value):
    if index == start == end:
        array[index] = value
        tree[node] = array[index]
    elif start <= index <= end:
        mid = (start+end)//2
        tree[node] = mod_mult(update(start, mid, node*2, index, value), update(mid+1, end, node*2+1, index, value), MOD)
    return tree[node]

def query(start, end, node, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return mod_mult(query(start, mid, node*2, left, right), query(mid+1, end, node*2+1, left, right), MOD)

for n in range(N):
    array.append(int(sys.stdin.readline()))

make(1,N,1)

for m in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, N, 1, b, c)
    if a == 2:
        print(query(1, N, 1, b, c))