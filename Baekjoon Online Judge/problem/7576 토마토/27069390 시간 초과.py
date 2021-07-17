from __future__ import annotations

import collections
import enum
import sys
import typing


class TOMATO_STATUS(enum.IntEnum):
    MATURE = 1
    IMMATURE = 0
    EMPTY = -1


class Box:
    class Node:
        def __init__(self, box:Box, y:int, x:int, status:TOMATO_STATUS):
            self.box = box
            self.x = x
            self.y = y
            self.status = status
            self.days_to_grow = 0 if (status == TOMATO_STATUS.MATURE) else sys.maxsize
            self.box.statistics[self.status] += 1
            if self.status == TOMATO_STATUS.MATURE:
                self.box.leaf.append(self)


        def __str__(self) -> str:
            return f'<Node: stat:{self.status}, days:{self.days_to_grow}>'


        def __repr__(self) -> str:
            return self.__str__()


        def set_status(self, status:TOMATO_STATUS):
            self.box.statistics[self.status] -= 1
            self.status = status
            self.box.statistics[self.status] += 1



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
            self.days_to_grow = src.days_to_grow+1
            self.set_status(TOMATO_STATUS.MATURE)

    
    def __init__(self, width:int, height:int, array_1d:typing.Iterable[TOMATO_STATUS]):
        self.height = height
        self.width = width
        self.area = height * width
        self.statistics = collections.defaultdict(lambda: 0) # Counter
        self.leaf:typing.List[Box.Node] = []
        self.list:typing.List[Box.Node] = [Box.Node(box=self, y=idx//width, x=idx%width, status=status) for idx, status in enumerate(array_1d)]


    def __getitem__(self, key:typing.Tuple[int, int]) -> Box.Node:
        y, x = key
        return self.list[y*self.width + x]

    
    def is_growable(self, src:Box.Node, dst: Box.Node) -> bool:
        if (src.days_to_grow+1 >= dst.days_to_grow):
            return False
        return (src.status == TOMATO_STATUS.MATURE) and (dst.status != TOMATO_STATUS.EMPTY)

    
    def bfs(self, root: Box.Node):
        deque:typing.Deque[typing.Tuple[Box.Node, Box.Node]] = collections.deque([(None, root)])
        while deque:
            parent, node = deque.popleft()
            if parent is not None:
                node.grow_from(parent)
            for child in node.get_growable_nodes():
                if self.is_growable(src=node, dst=child):
                    deque.append((node, child))
    
    
    def get_days_to_grow_all(self):
        retval = 0
        for node in self.list:
            if node.status == TOMATO_STATUS.MATURE:
                retval = max(retval, node.days_to_grow)
        return retval


WIDTH, HEIGHT = map(int, sys.stdin.readline().split())
ARRAY_ITERABLE = map(int, sys.stdin.read().split())

box = Box(WIDTH, HEIGHT, ARRAY_ITERABLE)

for node in box.leaf:
    box.bfs(node)
    if box.statistics[TOMATO_STATUS.IMMATURE]:
        print('-1')
        break
else:
    print(box.get_days_to_grow_all())
