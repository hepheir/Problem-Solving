import operator
import sys
import typing
from __future__ import annotations

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

OPERATOR_PRIORITY = {
    operator.add: 2,
    operator.sub: 2,
    operator.mul: 1,
    operator.floordiv: 1,
    None: sys.maxsize,
}


S = input()
TREE: typing.List[Node] = []

class Node:
    def __init__(self, x:int=None, op:function=None, left:Node=None, right:Node=None):
        self.x = x
        self.op = op
        self.left = left
        self.right = right

class Parser:
    buffer: typing.List[str] = []

    @classmethod
    def parse(cls, string):
        for c in string:
            if c == '-' and not cls.buffer:
                cls.buffer.append(c)
            elif c in OPERATORS:
                TREE.append(Node(
                    x=int(''.join(cls.buffer)),
                    op=(OPERATORS[c] if (c in OPERATORS) else None)
                ))
                cls.buffer.clear()
            else:
                cls.buffer.append(c)
        TREE.append(Node(
            x=int(''.join(cls.buffer).lstrip('0')),
            op=(OPERATORS[c] if (c in OPERATORS) else None)
        ))

Parser.parse(S)


def findMaxNodeIndex(list_of_nodes: typing.List[Node]) -> int:
    max_idx = 0
    max_node = list_of_nodes[max_idx]
    for idx, node in enumerate(list_of_nodes):
        if (node.x > max_node.x):
            max_idx = idx
            max_node = list_of_nodes[max_idx]
        elif (node.x == max_node.x) and (node.op_priority < max_node.op_priority):
            max_idx = idx
            max_node = list_of_nodes[max_idx]
    return max_idx


level = [Node(left=TREE[i], right=TREE[i+1]) for i in range(len(TREE)-1)]
if not level:  # 노드가 하나인 경우
    level = TREE

while len(level) > 1:
    max_idx = findMaxNodeIndex(level)
    max_node = level[max_idx]
    if max_node.child.left.parent.left is not None:
        max_node.child.left.parent.left.update(right=max_node)

    if max_node.child.right.parent.right is not None:
        max_node.child.right.parent.right.update(left=max_node)
    
    level.pop(max_idx)

print(level[0].x)
