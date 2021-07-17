from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

class NodeId(int):
    pass

class Tree:
    def __init__(self):
        self._connect = defaultdict(list)
        self._children = defaultdict(list)
        self._parent = defaultdict(lambda: None)
        self._subtreeSize = defaultdict(lambda: 1)

    def _setParent(self, node:NodeId, value:NodeId):
        self._parent[node] = value

    def _appendChild(self, node:NodeId, value:NodeId):
        self._children[node].append(value)

    def _make(self, current:NodeId, parent:NodeId):
        for node in self._connect[current]:
            if node != parent:
                self._appendChild(current, node)
                self._setParent(node, current)
                self._make(node, current)
                self._subtreeSize[current] += self._subtreeSize[node]

    def appendEdge(self, u:NodeId, v:NodeId):
        self._connect[u].append(v)
        self._connect[v].append(u)

    def makeTree(self, root:NodeId):
        self._make(root, None)
    
    def subtreeSize(self, node:NodeId) -> int:
        return self._subtreeSize[node]

if __name__ == "__main__":
    N, R, Q = map(int, input().split())
    tree = Tree()
    for n in range(N-1):
        U, V = map(int, input().split())
        tree.appendEdge(U-1, V-1)
    tree.makeTree(R-1)
    for q in range(Q):
        U = int(input())
        print(tree.subtreeSize(U-1))