import sys
input = sys.stdin.readline


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x0: int, y0: int, x1: int, y1: int):
        self.p = (Point(x0, y0), Point(x1, y1))
        self.x = (x0, x1)
        self.y = (y0, y1)
        self.parent = None
        self.subtree_size = 1


def CCW(l: Line, p: Point) -> int:
    # Line 기준 Point가 왼쪽인지 오른쪽인지 판별
    tmp = (l.x[0]*l.y[1] + l.x[1]*p.y + p.x*l.y[0]) \
        - (l.y[0]*l.x[1] + l.y[1]*p.x + p.y*l.x[0])
    if tmp > 0:
        return 1
    if tmp < 0:
        return -1
    return 0


def meets(l1: Line, l2: Line) -> bool:
    c1 = CCW(l1, l2.p[0]) * CCW(l1, l2.p[1])
    c2 = CCW(l2, l1.p[0]) * CCW(l2, l1.p[1])
    if c1 * c2 == 0:
        if max(l1.x) < min(l2.x):
            return False
        if max(l2.x) < min(l1.x):
            return False
        if max(l1.y) < min(l2.y):
            return False
        if max(l2.y) < min(l1.y):
            return False
        return True
    return c1 <= 0 and c2 <= 0

def find_ancestor(line:Line) -> Line:
    while line.parent is not None:
        line = line.parent
    return line

if __name__ == "__main__":
    N = int(input())
    lines = []
    for n in range(N):
        new_line = Line(*map(int, input().split()))
        for old_line in lines:
            new_ancestor = find_ancestor(new_line)
            old_ancestor = find_ancestor(old_line)
            if new_ancestor is old_ancestor:
                continue
            if meets(new_line, old_line):
                new_ancestor.parent = old_ancestor
                old_ancestor.subtree_size += new_ancestor.subtree_size
        lines.append(new_line)
    roots = 0
    max_size = 0
    for line in lines:
        if line is find_ancestor(line):
            roots += 1
            max_size = max(max_size, line.subtree_size)
    print(roots)
    print(max_size)