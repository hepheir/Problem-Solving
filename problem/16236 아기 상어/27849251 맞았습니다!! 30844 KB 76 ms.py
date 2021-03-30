import heapq
import sys


EMPTY_TILE = 0
SHARK_TILE = 9


class Shark:
    def __init__(self, space, x, y, size):
        self.space = space
        self.x = x
        self.y = y
        self.size = size
        self.hungry = size  # 내가 커지기 위해 먹어야 할 물고기 수
        self.moved = 0

    def goto_eat(self, y, x, dist):
        self.space[self.y][self.x] = EMPTY_TILE
        self.space[y][x] = SHARK_TILE
        self.moved += dist
        self.x = x
        self.y = y
        self.hungry -= 1
        if not self.hungry:
            self.size += 1
            self.hungry = self.size


class Space:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.space = [[*map(int, sys.stdin.readline().split())]
                      for n in range(self.n)]
        self.shark = self._find_shark()

    def _find_shark(self):
        for y in range(self.n):
            for x in range(self.n):
                if (self.space[y][x] == SHARK_TILE):
                    return Shark(self.space, x, y, 2)

    def is_edible(self, y, x):
        return (self.shark.size > self.space[y][x]) and (self.space[y][x] != EMPTY_TILE) and (self.space[y][x] != SHARK_TILE)

    def is_passable(self, y, x):
        return (self.shark.size >= self.space[y][x]) or (self.space[y][x] == SHARK_TILE)

    def move_if_movable(self):
        visited = dict()
        stack = [(self.shark.y, self.shark.x, 0)]
        heap = []
        while stack:
            while stack:
                y, x, dist = stack.pop()
                if visited.get((y, x), False):
                    continue
                visited[y, x] = True
                for cy, cx in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
                    if not ((0 <= cx < self.n) and (0 <= cy < self.n) and self.is_passable(cy, cx)):
                        continue
                    heapq.heappush(heap, (cy, cx, dist+1))
            while heap:
                y, x, dist = heapq.heappop(heap)
                if self.is_edible(y, x):
                    self.shark.goto_eat(y, x, dist)
                    return True
                stack.append((y,x, dist))
        return False


def solve():
    space = Space()

    while space.move_if_movable():
        pass

    return space.shark.moved


print(solve())
