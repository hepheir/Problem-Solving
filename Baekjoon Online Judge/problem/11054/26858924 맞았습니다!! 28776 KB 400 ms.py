MAX_N = 1000

class DP_Node:
    def __init__(self, value:int):
        self.value = value
        self.ascend = 1 # 증가수열길이
        self.descend = 1 # 감소수열길이
    
    def __repr__(self) -> str:
        return f'<value:{self.value} size:({self.ascend}, {self.descend})>'

N = int(input())
A = [DP_Node(a) for a in map(int, input().split())]

for i in range(N):
    for j in range(i):
        if not A[i].value > A[j].value: continue
        if A[i].ascend > A[j].ascend: continue
        A[i].ascend = A[j].ascend + 1

for i in range(N-1,-1,-1):
    for j in range(N-1, i,-1):
        if not A[i].value > A[j].value: continue
        if A[i].descend > A[j].descend: continue
        A[i].descend = A[j].descend + 1

pivot_node = max(A, key=lambda node: (node.ascend+node.descend))
print(pivot_node.ascend + pivot_node.descend - 1)