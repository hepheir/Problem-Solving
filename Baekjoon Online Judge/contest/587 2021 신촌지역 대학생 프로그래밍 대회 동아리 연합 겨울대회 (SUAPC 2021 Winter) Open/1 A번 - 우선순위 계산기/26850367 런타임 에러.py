import operator
import sys
import typing

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

OPERATOR_PRIORITY = {
    operator.add: 2,
    operator.sub: 2,
    operator.mul: 1,
    operator.truediv: 1,
    None: sys.maxsize,
}


class Node:
    class Edges:
        def __init__(self, left=None, right=None):
            self.left: Node = left
            self.right: Node = right

    def __init__(self, x: int = None, op: typing.Callable = None, left=None, right=None):
        self.parent = Node.Edges()
        self.child = Node.Edges(left, right)

        self.x: int = x
        self.op: function = op
        self.op_priority: int = OPERATOR_PRIORITY[self.op]

        if (left is not None) and (right is not None):
            self.update(left, right)

    def __str__(self) -> str:
        return f'<Node: x={self.x} op={str(self.op)}>'

    def __repr__(self) -> str:
        return self.__str__()

    def update(self, left=None, right=None):
        if left is not None:
            self.child.left = left
            self.child.left.parent.right = self
        if right is not None:
            self.child.right = right
            self.child.right.parent.left = self

        self.x = self.child.left.op(self.child.left.x, self.child.right.x)
        self.op = self.child.right.op
        self.op_priority = self.child.right.op_priority


S = input()

leaf: typing.List[Node] = []

# 수식 파싱, 말단 노드 생성
buffer: typing.List[str] = []
for c in S:
    if c == '-' and not buffer:
        buffer.append(c)
    elif c in OPERATORS:
        leaf.append(Node(
            x=int(''.join(buffer).lstrip('0')),
            op=(OPERATORS[c] if (c in OPERATORS) else None)
        ))
        buffer.clear()
    else:
        buffer.append(c)
leaf.append(Node(
    x=int(''.join(buffer).lstrip('0')),
    op=(OPERATORS[c] if (c in OPERATORS) else None)
))


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


level = [Node(left=leaf[i], right=leaf[i+1]) for i in range(len(leaf)-1)]
if not level:  # 노드가 하나인 경우
    level = leaf

while len(level) > 1:
    max_idx = findMaxNodeIndex(level)
    max_node = level[max_idx]
    if max_node.child.left.parent.left is not None:
        max_node.child.left.parent.left.update(right=max_node)

    if max_node.child.right.parent.right is not None:
        max_node.child.right.parent.right.update(left=max_node)
    
    level.pop(max_idx)

print(int(level[0].x) if (int(level[0].x) == level[0].x) else level[0].x)
