from __future__ import annotations

import collections
import enum
import sys
import time
import typing


sys.stdin = open('problem/7576 토마토/data/hepheir/worstcase/1.in', 'r')


class CheckTime_Node:
    def __init__(self):
        self.__last_start = 0
        self.total = 0
    
    def __str__(self):
        return str(self.total)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def start(self):
        self.__last_start = time.time()
        
    def end(self):
        self.total += time.time() - self.__last_start

CheckTime:typing.DefaultDict[CheckTime_Node] = collections.defaultdict(CheckTime_Node)


class TOMATO_STATUS(enum.IntEnum):
    MATURE = 1
    IMMATURE = 0
    EMPTY = -1


class Box:
    class Node:
        def __init__(self, box:Box, y:int, x:int, status:TOMATO_STATUS):
            CheckTime['Box.Node.__init__'].start()
            self.box = box
            self.x = x
            self.y = y
            self.status = status
            self.days_to_grow = 0 if (status == TOMATO_STATUS.MATURE) else sys.maxsize
            self.box.statistics[self.status] += 1
            if self.status == TOMATO_STATUS.MATURE:
                self.box.leaf.append(self)
            CheckTime['Box.Node.__init__'].end()


        def __str__(self) -> str:
            return f'<Node: stat:{self.status}, days:{self.days_to_grow}>'


        def __repr__(self) -> str:
            return self.__str__()


        def set_status(self, status:TOMATO_STATUS):
            CheckTime['Box.Node.set_status'].start()
            self.box.statistics[self.status] -= 1
            self.status = status
            self.box.statistics[self.status] += 1
            CheckTime['Box.Node.set_status'].end()



        def get_growable_nodes(self) -> typing.List[Box.Node]:
            CheckTime['Box.Node.get_growable_nodes'].start()
            retval = []
            if self.x > 0:
                retval.append(self.box[self.y, self.x-1])
            if self.y > 0:
                retval.append(self.box[self.y-1, self.x])
            if self.x < self.box.width-1:
                retval.append(self.box[self.y, self.x+1])
            if self.y < self.box.height-1:
                retval.append(self.box[self.y+1, self.x])
            CheckTime['Box.Node.get_growable_nodes'].end()
            return retval


        def grow_from(self, src:Box.Node):
            CheckTime['Box.Node.grow_from'].start()
            assert self.status != TOMATO_STATUS.EMPTY
            assert src.status == TOMATO_STATUS.MATURE
            self.days_to_grow = src.days_to_grow+1
            self.set_status(TOMATO_STATUS.MATURE)
            CheckTime['Box.Node.grow_from'].end()

    
    def __init__(self, width:int, height:int, array_1d:typing.Iterable[TOMATO_STATUS]):
        CheckTime['Box.__init__'].start()
        self.height = height
        self.width = width
        self.area = height * width
        self.statistics = collections.defaultdict(lambda: 0) # Counter
        self.leaf:typing.List[Box.Node] = []
        self.list:typing.List[Box.Node] = [Box.Node(box=self, y=idx//width, x=idx%width, status=status) for idx, status in enumerate(array_1d)]
        CheckTime['Box.__init__'].end()


    def __getitem__(self, key:typing.Tuple[int, int]) -> Box.Node:
        y, x = key
        return self.list[y*self.width + x]

    
    def is_growable(self, src:Box.Node, dst: Box.Node) -> bool:
        if (src.days_to_grow+1 >= dst.days_to_grow):
            return False
        return (src.status == TOMATO_STATUS.MATURE) and (dst.status != TOMATO_STATUS.EMPTY)

    
    def bfs(self, root: Box.Node):
        CheckTime['Box.bfs'].start()
        deque:typing.Deque[typing.Tuple[Box.Node, Box.Node]] = collections.deque([(None, root)])
        while deque:
            parent, node = deque.popleft()
            if parent is not None:
                node.grow_from(parent)
            for child in node.get_growable_nodes():
                if self.is_growable(src=node, dst=child):
                    deque.append((node, child))
        CheckTime['Box.bfs'].end()
    
    
    def get_days_to_grow_all(self):
        CheckTime['Box.get_days_to_grow_all'].start()
        retval = 0
        for node in self.list:
            if node.status == TOMATO_STATUS.MATURE:
                retval = max(retval, node.days_to_grow)
        CheckTime['Box.get_days_to_grow_all'].end()
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

print(CheckTime)