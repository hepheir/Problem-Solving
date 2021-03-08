import dataclasses
import heapq
import operator
import typing


@dataclasses.dataclass(order=True)
class Operator:
    result: int
    priority: int
    index: int
    operator: typing.Callable[[int, int], int]
    leftidx:int
    rightidx:int
    leftnum: int
    rightnum: int


def parse_expression(S):
    expression = []
    number = 0
    for c in S:
        if c.isdigit():
            number = number*10 + int(c)
        else:
            expression.append(number)
            number = 0
            if c == '+':
                expression.append((operator.add, 2))
            elif c == '-':
                expression.append((operator.sub, 2))
            elif c == '*':
                expression.append((operator.mul, 1))
            elif c == '/':
                expression.append((operator.floordiv, 1))
    expression.append(number)
    return expression


def solve():
    expression = parse_expression(input())
    n_operator = len(expression) // 2
    if not n_operator:
        return expression[0]
    heap:typing.List[Operator] = []
    operators:typing.List[Operator] = []
    for i, leftnum, (operator_function, operator_priority), rightnum in zip(range(n_operator), expression[::2], expression[1::2], expression[2::2]):
        op = Operator(
            result=-operator_function(leftnum, rightnum),
            priority=operator_priority,
            index=i,
            operator=operator_function,
            leftidx=i-1,
            rightidx=i+1,
            leftnum=leftnum,
            rightnum=rightnum)
        operators.append(op)
        heapq.heappush(heap, op)
    while len(heap) > 1:
        top = heapq.heappop(heap)
        if top.leftidx >= 0:
            left = operators[top.leftidx]
            left.rightnum = -top.result
            left.result = -left.operator(left.leftnum, left.rightnum)
            left.rightidx += 1
        if top.rightidx < n_operator:
            right = operators[top.rightidx]
            right.leftnum = -top.result
            right.result = -right.operator(right.leftnum, right.rightnum)
            right.leftidx -= 1
    return -heapq.heappop(heap).result

print(solve())
