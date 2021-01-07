import sys
input = sys.stdin.readline


class Lines:
    def __init__(self, n_of_lines: int):
        self.x0 = [None] * n_of_lines
        self.y0 = [None] * n_of_lines
        self.x1 = [None] * n_of_lines
        self.y1 = [None] * n_of_lines
        self.parent = [None] * n_of_lines
        self.subtree_size = [1] * n_of_lines
        self.pointer = 0

    def append(self, x0: int, y0: int, x1: int, y1: int) -> None:
        new_line = self.pointer
        self.x0[new_line] = x0
        self.y0[new_line] = y0
        self.x1[new_line] = x1
        self.y1[new_line] = y1
        for old_line in range(new_line):
            new_ancestor = self.find_ancestor(new_line)
            old_ancestor = self.find_ancestor(old_line)
            if new_ancestor is old_ancestor:
                continue
            if self.meets(new_line, old_line):
                self.parent[new_ancestor] = old_ancestor
                self.subtree_size[old_ancestor] += self.subtree_size[new_ancestor]
        self.pointer += 1

    def ccw(self, x0: int, y0: int, x1: int, y1: int, x2: int, y2: int) -> None:
        tmp = (x0*y1 + x1*y2 + x2*y0) - (y0*x1 + y1*x2 + y2*x0)
        if tmp > 0:
            return 1
        if tmp < 0:
            return -1
        return 0

    def meets(self, l1: int, l2: int) -> bool:
        c1 = self.ccw(self.x0[l1], self.y0[l1],
                      self.x1[l1], self.y1[l1],
                      self.x0[l2], self.y0[l2]) \
            * self.ccw(self.x0[l1], self.y0[l1],
                       self.x1[l1], self.y1[l1],
                       self.x1[l2], self.y1[l2])
        c2 = self.ccw(self.x0[l2], self.y0[l2],
                      self.x1[l2], self.y1[l2],
                      self.x0[l1], self.y0[l1]) \
            * self.ccw(self.x0[l2], self.y0[l2],
                       self.x1[l2], self.y1[l2],
                       self.x1[l1], self.y1[l1])
        if c1 * c2 == 0:
            if max([self.x0[l1], self.x1[l1]]) < min([self.x0[l2], self.x1[l2]]):
                return False
            if max([self.x0[l2], self.x1[l2]]) < min([self.x0[l1], self.x1[l1]]):
                return False
            if max([self.y0[l1], self.y1[l1]]) < min([self.y0[l2], self.y1[l2]]):
                return False
            if max([self.y0[l2], self.y1[l2]]) < min([self.y0[l1], self.y1[l1]]):
                return False
            return True
        return c1 <= 0 and c2 <= 0

    def find_ancestor(self, line: int) -> int:
        while self.parent[line] is not None:
            line = self.parent[line]
        return line


if __name__ == "__main__":
    N = int(input())
    LINES = Lines(N)
    for n in range(N):
        LINES.append(*map(int, input().split()))
    roots = 0
    max_size = 0
    for line in range(LINES.pointer):
        if LINES.parent[line] is None:
            roots += 1
            max_size = max(max_size, LINES.subtree_size[line])
    print(roots)
    print(max_size)
