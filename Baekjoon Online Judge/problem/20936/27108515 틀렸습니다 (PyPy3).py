import dataclasses
import operator
import typing


@dataclasses.dataclass(order=True)
class Node:
    result_inverted: int
    oper_priority: int
    list_index: int

    oper_function: typing.Callable[[int, int], int] = dataclasses.field(repr=False, compare=False)
    left_number: int = dataclasses.field(repr=False, compare=False)
    right_number: int = dataclasses.field(repr=False, compare=False)
    left_term_list_index: int = dataclasses.field(repr=False, compare=False)
    right_term_list_index: int = dataclasses.field(repr=False, compare=False)

    heap_index: int = dataclasses.field(default=-1, repr=False, compare=False)

    def update_result(self):
        self.result = self.oper_function(self.left_number, self.right_number)

    @property
    def result(self) -> int:
        return -self.result_inverted
    
    @result.setter
    def result(self, value:int):
        self.result_inverted = -value


class Heap:
    def __init__(self, array:typing.List[Node]):
        self.list = array
        self.heap = (array.copy())
        self._heapify()

    
    def _heapify(self):
        n = len(self.heap)
        for i in reversed(range(n//2)):
            self._siftup(i)
    

    def push(self, item):
        self.heap.append(item)
        self._siftdown(0, len(self.heap)-1)
    

    def pop(self):
        lastelt = self.heap.pop()
        if self.heap:
            top = self.heap[0]
            self.heap[0] = lastelt
            self.heap[0].heap_index = 0
            if top.left_term_list_index >= 0:
                left = self.list[top.left_term_list_index]
                left.right_number = top.result
                left.update_result()
                left.right_term_list_index += 1
                if left.heap_index >= 0:
                    self._siftup(left.heap_index)
            if top.right_term_list_index < len(self.list):
                right = self.list[top.right_term_list_index]
                right.left_number = top.result
                right.update_result()
                right.left_term_list_index -= 1
                if right.heap_index >= 0:
                    self._siftup(right.heap_index)
            self._siftup(0)
            return top
        return lastelt
    

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                self.heap[pos].heap_index = pos
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
        self.heap[pos].heap_index = pos


    def _siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        childpos = 2*pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            self.heap[pos].heap_index = pos
            pos = childpos
            childpos = 2*pos + 1
        self.heap[pos] = newitem
        self.heap[pos].heap_index = pos
        self._siftdown(startpos, pos)


def parse_expression(S):
    expression = []
    number = 0
    for c in S:
        if c.isdigit():
            number = number*10 + int(c)
            continue
        expression.append(number)
        if c == '+': expression.append((operator.add, 2))
        elif c == '-': expression.append((operator.sub, 2))
        elif c == '*': expression.append((operator.mul, 1))
        elif c == '/': expression.append((operator.floordiv, 1))
        number = 0
    expression.append(number)
    return expression


def make_heap_from_expression(expression:list):
    node_list:typing.List[Node] = []
    n_operator = len(expression) // 2
    # 노드 및 우선순위 큐 생성
    for i in range(n_operator):
        left_number, right_number = expression[i*2], expression[i*2+2]
        oper_function, oper_priority = expression[i*2+1]
        node = Node(
            result_inverted=-oper_function(left_number, right_number),
            oper_priority=oper_priority,
            list_index=i,
            oper_function=oper_function,
            left_number=left_number,
            right_number=right_number,
            left_term_list_index=i-1,
            right_term_list_index=i+1)
        node_list.append(node)
    return Heap(node_list)


expression = parse_expression(S=input())

if len(expression) == 1:
    print(expression[0])
else:
    heap = make_heap_from_expression(expression)
    while heap.heap:
        node = heap.pop()
    print(node.result)
