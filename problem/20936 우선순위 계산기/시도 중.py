from __future__ import annotations

import dataclasses
import operator
import typing


class heapq:
    def __init__(self):
        self._list:typing.List[OperatorNode] = []


    def __getitem__(self, key) -> OperatorNode:
        return self._list[key]
    

    def __setitem__(self, key:int, item:OperatorNode):
        self._list[key] = item
        item.heap_idx = key


    @property
    def isempty(self):
        return not self._list


    @property
    def size(self):
        return len(self._list)

    
    def heappos(self, item:OperatorNode):
        return item.heap_idx


    # 파이썬 heapq 모듈에서 가져옴
    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self._list.append(item)
        self.siftdown(0, self.size-1)


    # 파이썬 heapq 모듈에서 가져옴
    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self._list.pop()    # raises appropriate IndexError if heap is empty
        if self:
            returnitem = self[0]
            self[0] = lastelt
            self.siftup(0)
            return returnitem
        return lastelt


    # 파이썬 heapq 모듈에서 가져옴
    def siftdown(self, startpos, pos):
        newitem = self[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self[parentpos]
            if newitem < parent:
                self[pos] = parent
                pos = parentpos
                continue
            break
        self[pos] = newitem


    # 파이썬 heapq 모듈에서 가져옴
    def siftup(self, pos):
        endpos = self.size
        startpos = pos
        newitem = self[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self[childpos] < self[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self[pos] = self[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self[pos] = newitem
        self.siftdown(startpos, pos)


@dataclasses.dataclass(unsafe_hash=True)
class OperatorNode:
    operator: typing.Callable[[int, int], int]
    priority: int
    order: int
    left:NumberNode = dataclasses.field(default=None)
    right:NumberNode = dataclasses.field(default=None)
    heap_idx:int = dataclasses.field(default=None)

    @property
    def value(self):
        return self.operator(self.left.value, self.right.value)
    

    def __lt__(self, node:OperatorNode) -> bool:
        if (self.value > node.value):
            return True
        if (self.value < node.value):
            return False
        if (self.priority > node.priority):
            return True
        if (self.priority < node.priority):
            return False
        return self.order < node.order


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


def solve():
    linkedList = LinkedList()
    heap = heapq()

    S = input()
    number = 0
    for c in S:
        if c.isdigit():
            number = number*10 + int(c)
            continue
        linkedList.pushback(NumberNode(number))
        number = 0
        if c == '+':
            operatorNode = OperatorNode(operator.add, 0, linkedList.n_operators)
        elif c == '-':
            operatorNode = OperatorNode(operator.sub, 0, linkedList.n_operators)
        elif c == '*':
            operatorNode = OperatorNode(operator.mul, 1, linkedList.n_operators)
        elif c == '/':
            operatorNode = OperatorNode(operator.floordiv, 1, linkedList.n_operators)
        else:
            continue
        linkedList.pushback(operatorNode)
        linkedList.n_operators += 1
    linkedList.pushback(NumberNode(number))
    
    node:OperatorNode = linkedList.front.right
    while node is not None:
        heap.heappush(node)
        node = node.right.right

    if heap.isempty:
        print(linkedList.front.value)
        return

    while heap.size > 1:
        linkedList.remove_operator(heap[0])
        node = heap.heappop()
        if node.left.left is not None:
            heap.siftup(heap.heappos(node.left.left))
        if node.right.right is not None:
            heap.siftup(heap.heappos(node.right.right))
    print(heap[0].value)

solve()
