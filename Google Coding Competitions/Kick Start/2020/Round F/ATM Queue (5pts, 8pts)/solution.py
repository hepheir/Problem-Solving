import sys
import collections
input = sys.stdin.readline

def solve(n_of_people:int, max_w_amount:int, w_amounts:list):
    queue = collections.deque([(i+1, req) for i, req in enumerate(w_amounts)])
    while queue:
        i, required = queue.popleft()
        required -= max_w_amount
        if required > 0:
            queue.append((i, required))
        else:
            yield i


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        ans = solve(N, X, A)
        print('Case #{0}: {1}'.format(t+1, " ".join(map(str, ans))))