MAX_N = 1000

class DP_Node:
    def __init__(self, value:int):
        self.value = value
        self.descend = 1 # 감소수열길이

N = int(input())
A = [DP_Node(a) for a in map(int, input().split())]

for i in range(N-1,-1,-1):
    for j in range(N-1, i,-1):
        if not A[i].value > A[j].value: continue
        if A[i].descend > A[j].descend: continue
        A[i].descend = A[j].descend + 1

pivot_node = max(A, key=lambda node: node.descend)
print(pivot_node.descend)