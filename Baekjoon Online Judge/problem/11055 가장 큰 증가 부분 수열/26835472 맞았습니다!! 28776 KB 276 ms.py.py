import sys

class Node:
    def __init__(self, value:int):
        self.value:int = value
        self.sum:int = value
    
    def sequence(self):
        node = self
        while node is not None:
            yield node.value
            node = node.parent

N = int(sys.stdin.readline())
A = [Node(Ai) for Ai in map(int, sys.stdin.readline().split())]

for current in range(N):
    for parent in range(current+1):
        if not (A[parent].value < A[current].value):
            continue
        if A[parent].sum > (A[current].sum - A[current].value):
            A[current].sum = A[parent].sum + A[current].value

print(max(A, key=lambda node: node.sum).sum)
