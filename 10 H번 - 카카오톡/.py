import sys
from __future__ import annotations

class Line:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c
    
    def does_intersect(self, line:Line) -> bool:
        return (line.a * self.b) == (self.a * line.b)

N = int(sys.stdin.readline())
A = [Line(*map(int, sys.stdin.readline().split())) for n in range(N)]

for i in range(N):
    for j in range(i):
        pass