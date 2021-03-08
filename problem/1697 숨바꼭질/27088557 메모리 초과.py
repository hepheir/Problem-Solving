import collections

def solve(n, k):
    stack = [n]
    buffer = set()
    visited = set()
    depth = 0    
    while stack:
        for x in stack:
            if x == k:
                return depth
            buffer.add(x*2)
            buffer.add(x-1)
            buffer.add(x+1)
        buffer -= visited
        visited.update(buffer)
        stack.clear()
        stack.extend(buffer)
        depth += 1

N, K = map(int, input().split())

print(solve(N, K))