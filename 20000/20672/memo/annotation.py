import sys
import math
from __future__ import annotations

# WARNING THIS IS FOR DEBUGGING
sys.stdin = open(f'20000/20672/data/boj.sample.{1}.in', 'r')


class State:
    """
    Available States:
      -1: Root
       0: Opened
       1: Connected
       2: Closed
    """

    def get_state_outs(state_in):
        if state_in == -1:
            # (o)
            yield True, 0, None
            yield True, 2, None
        elif state_in == 0:
            # (o)
            yield True, 1, 1
            yield True, 1, 2
            yield True, 2, 1
            yield True, 2, 2
            # (x)
            yield False, 0, 2
            yield False, 2, 0
            yield False, 2, 2
        elif state_in == 1:
            # (o)
            yield True, 1, 1
            yield True, 1, 2
            yield True, 2, 1
            yield True, 2, 2
            # (x)
            yield False, 2, 2
        elif state_in == 2:
            # (x)
            yield False, 2, 2


class Node:
    def __init__(self, number:int, genom:int):
        self.number = number
        self.genom = genom
        self.parent = None
        self.children = []
        self.subtree = { 
            0: 0,
            1: 0,
            2: 0,
        }

    def predict(self, state_in):
        for child in self.children:
            for state in State.get_state_outs(state_in)


class Tree:
    def __init__(self):
        self.N = int(sys.stdin.readline())
        g = [0, *map(int, sys.stdin.readline().split())]

        self.graph = [list() for _ in range(self.N+1)]
        self.nodes = [Node(i, g[i]) for i in range(self.N+1)]

        for n in range(self.N-1):
            u, v = map(int, sys.stdin.readline().split())
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.nodes[1].state_in = -1
        self.build_subtree(1, None)

    def build_subtree(self, root:int, parent:int, state_in:State.STATE):
        for child in self.graph[root]:
            if child == parent:
                continue
            self.nodes[root].children.append(self.nodes[child])
            self.nodes[child].parent = self.nodes[root]
            for state_out in State.get_state_out(state_in, State.O):
                self.build_subtree(child, root, state_out)
            for state_out in State.get_state_out(state_in, State.X):
                self.build_subtree(child, root, state_out)
