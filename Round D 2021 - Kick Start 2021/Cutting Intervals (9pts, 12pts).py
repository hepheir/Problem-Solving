from sys import stdin
from collections import Counter


def main():
    testcases = int(stdin.readline())

    for _ in range(testcases):
        N, C = map(int, stdin.readline().split())
        L = []
        R = []
        for n in range(N):
            l, r = map(int, stdin.readline().split())
            L.append(l)
            R.append(r)
        answer = solve(N, C, L, R)
        print(f'Case #{testcases}: {answer}')



def solve(N, C, L, R):
    cutable_counter = Counter()
    n_intervals = N
    for l, r in zip(L, R):
        for cutable_spot in range(l+1, r):
            cutable_counter[cutable_spot] += 1
    for x, cutables in cutable_counter.most_common(C):
        n_intervals += cutables
    return n_intervals


if __name__ == "__main__":
    main()