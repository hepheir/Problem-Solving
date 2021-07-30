from __future__ import annotations
import sys
import typing


class Stack:
    top:Stack.Node = None
    size = 0

    class Node:
        def __init__(self, parent, data):
            self.parent = parent
            self.data = data

    @classmethod
    def push(cls, data):
        cls.top = cls.Node(cls.top, data)
        cls.size += 1
    
    @classmethod
    def pop(cls):
        node = cls.top
        cls.top = cls.top.parent
        cls.size -= 1
        return node.data

    @classmethod
    def empty(cls):
        return cls.size == 0

class Point:
    def __init__(self, x_pos: int, open: int, close: int):
        self.x = x_pos
        self.open = open  # 왼쪽으로 뻗어나가는 원
        self.close = close  # 오른쪽으로 뻗어나가는 원


class Axis:
    axis: typing.List[Point] = []  # 정렬된 상태를 유지하는 리스트

    @classmethod
    def insert_point(cls, point: Point):
        if cls.axis:
            cls.bin_search(0, len(cls.axis)-1, point)
        else:
            cls.axis.append(point)

    @classmethod
    def bin_search(cls, start: int, end: int, point: Point):
        mid = (start+end)//2
        p = cls.axis[mid]
        # 이미 있으면 합침
        if point.x == p.x:
            p.open += point.open
            p.close += point.close
        # 없으면 삽입
        elif start == end:
            if point.x < p.x:
                cls.axis.insert(mid, point)
            else:
                cls.axis.insert(mid+1, point)
        else:
            if point.x < p.x:
                return cls.bin_search(start, mid, point)
            else:
                return cls.bin_search(mid+1, end, point)


class State:
    Connected = '<Connected>'
    NotConnected = '<NotConnected>'


vertices = dict()  # {X:(LEFT_CNT, RIGHT_CNT)}
for n in range(int(sys.stdin.readline())):
    x, r = map(int, sys.stdin.readline().split())
    Axis.insert_point(Point(x-r, open=1, close=0))
    Axis.insert_point(Point(x+r, open=0, close=1))

answer = 1
for point in Axis.axis:
    if point.close:
        for _ in range(point.close):
            if Stack.pop() == State.Connected:
                answer += 2
            else:
                answer += 1
    if point.open:
        for _ in range(point.open-1):
            Stack.push(State.Connected)
        Stack.push(State.NotConnected)
    if not Stack.empty() and not point.open:
        Stack.pop()
        Stack.push(State.NotConnected)
print(answer)
