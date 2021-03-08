import collections

TELEPORT = 1
WALK_FRONT = 2
WALK_BACK = 3

def solve(n, k):
    deque = collections.deque([(n, None)])
    depth = 0    
    while True:
        width = len(deque) # 같은 depth 상의 노드 갯수
        for w in range(width):
            x, last_op = deque.popleft()
            if (x < 0) or (100000 < x):
                continue
            if x == k:
                return depth
            if last_op == WALK_FRONT:
                deque.append((x+1, WALK_FRONT))
                deque.append((x-1, WALK_BACK))
            elif last_op == WALK_BACK:
                deque.append((x*2, TELEPORT))
                deque.append((x-1, WALK_BACK))
            else:
                deque.append((x*2, TELEPORT))
                deque.append((x+1, WALK_FRONT))
                deque.append((x-1, WALK_BACK))
        depth += 1

N, K = map(int, input().split())

print(solve(N, K))