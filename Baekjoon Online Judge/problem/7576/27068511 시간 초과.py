from __future__ import annotations

import collections
import enum
import sys
import typing

sys.setrecursionlimit(int(1e6))


class TOMATO_STATUS(enum.IntEnum):
    MATURE = 1
    IMMATURE = 0
    EMPTY = -1


class Box:
    class Node:
        def __init__(self, box:Box, y:int, x:int, tomato_status:TOMATO_STATUS):
            self.box = box
            self.x = x
            self.y = y
            self.status = tomato_status
            self.passed_days = sys.maxsize


        def __str__(self) -> str:
            return f'<Node: stat:{self.status}, days:{self.passed_days}>'


        def __repr__(self) -> str:
            return self.__str__()


        def get_growable_nodes(self) -> typing.Generator[Box.Node, None, None]:
            if self.x > 0:
                yield self.box[self.y, self.x-1]
            if self.y > 0:
                yield self.box[self.y-1, self.x]
            if self.x < self.box.width-1:
                yield self.box[self.y, self.x+1]
            if self.y < self.box.height-1:
                yield self.box[self.y+1, self.x]


        def grow_from(self, src:Box.Node):
            assert self.status != TOMATO_STATUS.EMPTY
            assert src.status == TOMATO_STATUS.MATURE
            self.passed_days = src.passed_days+1
            self.status = TOMATO_STATUS.MATURE

    
    def __init__(self, width:int, height:int, array_1d:typing.Iterable[TOMATO_STATUS]):
        self.list:typing.List[Box.Node] = [Box.Node(box=self, y=idx//width, x=idx%width, tomato_status=status) for idx, status in enumerate(array_1d)]
        self.height = height
        self.width = width
        self.area = height * width


    def __getitem__(self, key:typing.Tuple[int, int]) -> Box.Node:
        y, x = key
        return self.list[y*self.width + x]

    
    def is_growable(self, src:Box.Node, dst: Box.Node) -> bool:
        if (src.passed_days+1 >= dst.passed_days):
            return False
        if (src.status != TOMATO_STATUS.MATURE):
            return False
        if (dst.status == TOMATO_STATUS.EMPTY):
            return False
        return True


    # def dfs(self, root: Box.Node):
    #     for node in root.get_growable_nodes():
    #         if self.is_growable(src=root, dst=node):
    #             node.grow_from(root)
    #             self.dfs(node)

    
    def bfs(self, root: Box.Node):
        deque:typing.Deque[typing.Tuple[Box.Node, Box.Node]] = collections.deque([(None, root)])
        while deque:
            parent, node = deque.popleft()
            if parent is not None:
                node.grow_from(parent)
            for child in node.get_growable_nodes():
                if self.is_growable(src=node, dst=child):
                    deque.append((node, child))


WIDTH, HEIGHT = map(int, sys.stdin.readline().split())
ARRAY_ITERABLE = map(int, sys.stdin.read().split())

box = Box(WIDTH, HEIGHT, ARRAY_ITERABLE)

start_at = []
for node in box.list:
    if node.status == TOMATO_STATUS.MATURE:
        node.passed_days = 0
        start_at.append(node)

for node in start_at:
    box.bfs(node)

minimun_passed_days = 0
for node in box.list:
    if (node.status == TOMATO_STATUS.IMMATURE):
        print('-1')
        break
    if (node.status == TOMATO_STATUS.MATURE):
        minimun_passed_days = max(node.passed_days, minimun_passed_days)
else:
    print(minimun_passed_days)
