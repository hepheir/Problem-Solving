from __future__ import annotations

from sys import stdin, stdout
from math import gcd
from typing import Iterable

MOD = 10**9+7

class Modded:
    MOD = 10**9+7

    def sum(a, b):
        return ((a % MOD) + (b % MOD)) % MOD
    
    def mul(a, b):
        return ((a % MOD) * (b % MOD)) % MOD

class Node:
    def __init__(self, tree:Tree, id:int, genom:int):
        self.tree = tree
        self.id = id
        self.g = genom
        self.level = 0
        self.parent = None
        self.is_leaf = False
        self.dp_o = 1 # 자신이 o일 때, 서브트리 경우의 수
        self.dp_x = 1 # 자신이 x일 때, 서브트리 경우의 수
    
    def __str__(self):
        return f'''<Node:{self.id}, {f"par:{self.parent.id}" if self.parent else "root"}>'''
    
    def __repr__(self):
        return self.__str__()
    
    def path(self)->Iterable[Node]:
        node = self
        while node.parent is not None:
            yield node
            node = node.parent
    
    def child(self)->Iterable[Node]:
        for child_id in self.tree.graph[self.id]:
            child = self.tree.nodes[child_id]
            if child is not self.parent:
                yield child

    def sibling(self)->Iterable[Node]:
        for child in self.parent.child:
            if child is not self:
                yield child


class Tree:
    def __init__(self, root_id:int=0):
        self.size = int(stdin.readline())
        self.nodes = [Node(self, id, gen) for id, gen in zip(range(self.size), map(int, stdin.readline().split()))]
        self.graph = [list() for _ in range(self.size)]
        for n in range(self.size-1):
            u, v = map(lambda x: int(x)-1, stdin.readline().split())
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.root = self.nodes[root_id]
        self.leaf = list(sorted(self.make(root_id), key=lambda n: n.id))

    def make(self, root_id:int)->None:
        # DFS with stack, post-order traversal
        s1 = [root_id]
        s2 = []
        while s1:
            node = self.nodes[s1.pop()] 
            s2.append(node)
            for child in node.child():
                child.parent = node
                child.level = node.level + 1
                s1.append(child.id)
        while s2:
            node = s2.pop()
            children = list(node.child())
            for child in children:
                node.dp_o = Modded.mul(node.dp_o, child.dp_o+1)
                node.dp_x = Modded.sum(node.dp_x, child.dp_o + child.dp_x - 1)
            if not children:
                node.is_leaf = True
                yield node


def solve(leaf_node:Node)->int:
    # 경로상에 군집이 없는 경우 + 자신이 (x)이며 '형제 노드의 서브트리'상에 적어도 하나의 (o)가 있는 경우
    count = 1
    cheatkey = tree.root.g
    child = None
    for node in leaf_node.path(): # log(n)
        if child:
            count = Modded.sum(count, node.dp_x - (child.dp_o + child.dp_x))
        child = node
    answer = Modded.mul(cheatkey, count)
    # 경로상에 군집이 걸치는 깊이의 시작(i)~끝(j)을 상정하고 계산
    for i in range(1, leaf_node.level+1):  # log(n)
        for j in range(i, leaf_node.level+1):  # log(n)
            count = 1
            cheatkey = tree.root.g
            child = None
            for node in leaf_node.path():  # log(n)
                if i <= node.level <= j:
                    cheatkey = gcd(node.g, cheatkey)
                    if child:
                        count = Modded.mul(count, (node.dp_o) // (child.dp_o + 1))
                child = node
            answer = Modded.sum(answer, Modded.mul(cheatkey, count))
    return answer

tree = Tree()
stdout.write(' '.join((str(solve(n)) for n in tree.leaf)))