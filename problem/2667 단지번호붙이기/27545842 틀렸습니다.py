import collections
import sys

N = int(sys.stdin.readline())
MAP = [[*map(int, sys.stdin.readline().rstrip())] for n in range(N)]

deque = collections.deque()
visited = collections.defaultdict(lambda: False)
building_complex = []

for y in range(N):
    for x in range(N) :
        if MAP[y][x]:
            deque.append((y,x))

def dfs(y,x):
    if visited[y,x] or not MAP[y][x]:
        return
    visited[y,x] = True
    building_complex[-1] += 1
    if x > 0:
        dfs(y,x-1)
    if x < N-1:
        dfs(y,x+1)
    if y > 0:
        dfs(y-1,x)
    if y < N-1:
        dfs(y+1,x)

while deque:
    y, x = deque.popleft()
    if not visited[y,x]:
        building_complex.append(0)
        dfs(y, x)

print(len(building_complex))
print('\n'.join(map(str, building_complex)))
