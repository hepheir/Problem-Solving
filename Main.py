import sys
input = sys.stdin.readline


class Line(list):
    pass


class LineId(int):
    pass


def ccw(x0: int, y0: int, x1: int, y1: int, x2: int, y2: int) -> int:
    return (x0*y1 + x1*y2 + x2*y0) - (y0*x1 + y1*x2 + y2*x0)


class Main:
    def __init__(self):
        self.N = int(input())
        self.lines = [list(map(int, input().split())) for n in range(self.N)]
        self.parents = [n for n in range(self.N)]
        self.sizes = [1] * self.N

    def solve(self):
        roots = 0
        maxsize = 0
        for i in range(self.N-1):
            for j in range(i, self.N):
                i_parent = self.find_ancestor(i)
                j_parent = self.find_ancestor(j)
                if i_parent == j_parent:
                    continue
                if self.does_meet(i, j):
                    self.merge_groups(j, i)
        for line in range(self.N):
            if self.is_root(line):
                roots += 1
                maxsize = max(maxsize, self.sizes[line])
        print(roots)
        print(maxsize)

    def find_ancestor(self, line: LineId) -> LineId:
        if self.parents[line] == line:
            return line
        self.parents[line] = self.find_ancestor(self.parents[line])
        return self.parents[line]

    def is_root(self, line: LineId) -> bool:
        return line == self.find_ancestor(line)

    def does_meet(self, line1: int, line2: int) -> bool:
        c1 = ccw(
            *self.lines[line1],
            *self.lines[line2][:2]
        ) * ccw(
            *self.lines[line1],
            *self.lines[line2][2:]
        )
        c2 = ccw(
            *self.lines[line2],
            *self.lines[line1][:2]
        ) * ccw(
            *self.lines[line2],
            *self.lines[line1][2:]
        )
        # 일직선 상에 놓인경우, 직선이 곂치는지 검사
        if c1 == c2 == 0:
            if self.lines[line1][0] > self.lines[line2][0]:
                line1, line2 = line2, line1
            if max(self.lines[line1][::2]) < min(self.lines[line2][::2]):
                return False
            if max(self.lines[line1][1::2]) < min(self.lines[line2][1::2]):
                return False
            return True
        # 그렇지 않은 경우, 교차하는지 검사
        else:
            return c1 <= 0 and c2 <= 0

    def merge_groups(self, line1: LineId, line2: LineId):
        line1_parent = self.find_ancestor(line1)
        line2_parent = self.find_ancestor(line2)
        # 트리의 사이클 발생으로 인한 무한 루프 방지
        if line1_parent > line2_parent:
            line1_parent, line2_parent = line2_parent, line1_parent
        self.parents[line2_parent] = line1_parent
        self.sizes[line1_parent] += self.sizes[line2_parent]


if __name__ == "__main__":
    Main().solve()
