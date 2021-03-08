import collections
import sys
import typing

MATURE = 1
IMMATURE = 0
EMPTY = -1


class Box:
    class Node:
        def __init__(self, box, y, x, status):
            self.box = box
            self.x = x
            self.y = y
            self.status = status
            self.days_to_grow = 0 if (status == MATURE) else sys.maxsize
            if self.status == MATURE:
                self.box.leaf.append(self)


        def set_status(self, status):
            self.status = status


        def get_neighbour_nodes(self):
            if self.x > 0:
                yield self.box[self.y, self.x-1]
            if self.y > 0:
                yield self.box[self.y-1, self.x]
            if self.x < self.box.width-1:
                yield self.box[self.y, self.x+1]
            if self.y < self.box.height-1:
                yield self.box[self.y+1, self.x]


        def grow_from(self, src):
            self.days_to_grow = src.days_to_grow+1
            self.set_status(MATURE)

    
    def __init__(self, width, height, array_1d):
        self.height = height
        self.width = width
        self.leaf = []
        self.list = [Box.Node(box=self, y=idx//width, x=idx%width, status=status) for idx, status in enumerate(array_1d)]


    def __getitem__(self, key):
        y, x = key
        return self.list[y*self.width + x]

    
    def is_growable(self, src, dst):
        if (src is None):
            return True
        if (src.days_to_grow+1 >= dst.days_to_grow):
            return False
        return (src.status == MATURE) and (dst.status != EMPTY)

    
    def bfs(self):
        deque = collections.deque()
        for leaf_node in self.leaf:
            for neighbour_node in leaf_node.get_neighbour_nodes():
                if self.is_growable(src=leaf_node, dst=neighbour_node):
                    deque.append((leaf_node, neighbour_node))
        while deque:
            parent, node = deque.popleft()
            if self.is_growable(src=parent, dst=node):
                node.grow_from(parent)
                deque.extend([(node, child) for child in node.get_neighbour_nodes()])


WIDTH, HEIGHT = map(int, sys.stdin.readline().split())
ARRAY_ITERABLE = map(int, sys.stdin.read().split())

box = Box(WIDTH, HEIGHT, ARRAY_ITERABLE)
box.bfs()
days_to_grow_all = 0
for node in box.list:
    if node.status == IMMATURE:
        print('-1')
        break
    if node.status == MATURE:
        days_to_grow_all = max(days_to_grow_all, node.days_to_grow)
else:
    print(days_to_grow_all)
