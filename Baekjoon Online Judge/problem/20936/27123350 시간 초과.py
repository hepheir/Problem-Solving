from __future__ import annotations

import dataclasses
import operator
import typing


@dataclasses.dataclass()
class OperatorNode:
    operator: typing.Callable[[int, int], int]
    priority: int
    left:NumberNode = dataclasses.field(default=None)
    right:NumberNode = dataclasses.field(default=None)

    @property
    def value(self):
        return self.operator(self.left.value, self.right.value)


@dataclasses.dataclass()
class NumberNode:
    value: int
    left:OperatorNode = dataclasses.field(default=None)
    right:OperatorNode = dataclasses.field(default=None)


@dataclasses.dataclass()
class LinkedList:
    front:NumberNode = dataclasses.field(default=None)
    rear:NumberNode = dataclasses.field(default=None)
    n_operators:int = dataclasses.field(default=0)

    @property
    def expression(self):
        retval = ''
        node = self.front
        for i in range(self.n_operators*2+1):
            if i % 2:
                retval += {
                    operator.add: '+',
                    operator.sub: '-',
                    operator.mul: '*',
                    operator.floordiv: '/',
                }[node.operator]
            else:
                retval += str(node.value)
            node = node.right
        return retval



    def pushback(self, node:typing.Union[OperatorNode, NumberNode]):
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.right = node
            node.left = self.rear
            self.rear = node
    
    def remove_operator(self, node:OperatorNode):
        # 자신(연산자노드)과 자신의 오른쪽 노드(숫자노드)를 지움
        node.left.value = node.value
        node.left.right = node.right.right
        if node.right.right is not None:
            node.right.right.left = node.left
        self.n_operators -= 1

    
    def pop(self):
        node:OperatorNode = self.front.right
        return_node = node
        while node is not None:
            if (node.value > return_node.value) or ((node.value == return_node.value) and (node.priority > return_node.priority)):
                return_node = node
            node = node.right.right
        return return_node

if __name__ == '__main__':
    linkedList = LinkedList()

    S = input()
    number = 0
    for c in S:
        if c.isdigit():
            number = number*10 + int(c)
            continue
        linkedList.pushback(NumberNode(number))
        if c == '+':
            linkedList.pushback(OperatorNode(operator.add, 0))
            linkedList.n_operators += 1
        elif c == '-':
            linkedList.pushback(OperatorNode(operator.sub, 0))
            linkedList.n_operators += 1
        elif c == '*':
            linkedList.pushback(OperatorNode(operator.mul, 1))
            linkedList.n_operators += 1
        elif c == '/':
            linkedList.pushback(OperatorNode(operator.floordiv, 1))
            linkedList.n_operators += 1
        number = 0
    linkedList.pushback(NumberNode(number))
    
    if not linkedList.n_operators:
        print(linkedList.front.value)
    else:
        node = linkedList.pop()
        while linkedList.n_operators > 1:
            linkedList.remove_operator(node)
            node = linkedList.pop()
        print(node.value)
