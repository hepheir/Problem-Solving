import sys
input = sys.stdin.readline


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'{str(self.x)}, {str(self.y)}'
    
    def __repr__(self) -> str:
        return self.__str__()


class Line:
    def __init__(self, x0: int, y0: int, x1: int, y1: int):
        self.p = (Point(x0, y0), Point(x1, y1))
        self.x = (x0, x1)
        self.y = (y0, y1)
        self.parent = None
        self.subtree_size = 1

    def __str__(self):
        return str(self.p)

    def __repr__(self) -> str:
        return self.__str__()


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

if __name__ == "__main__":
    N = int(input())
    lines = []
    for n in range(N):
        new_line = Line(*map(int, input().split()))
        lines.append(new_line)
    for i in range(N-1):
        for j in range(i+1, N):
            l1 = lines[i]
            l2 = lines[j]
            if l1 is l2:
                continue
            if meets(l1, l2):
                while l1.parent is not None:
                    l1 = l1.parent
                while l2.parent is not None:
                    l2 = l2.parent
                l1.parent = l2
                l2.subtree_size += l1.subtree_size
    roots = 0
    max_size = 0
    for line in lines:
        if line.parent is None:
            roots += 1
            max_size = max(max_size, line.subtree_size)
    print(roots)
    print(max_size)