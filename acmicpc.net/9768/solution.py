import sys


T = int(sys.stdin.readline())
for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    suit = [[] for _ in range(m)]
    for _ in range(k):
        r, s = map(int, sys.stdin.readline().split())
        suit[s-1].append(r)

    max_seqlen = 0
    for s in range(m):
        suit[s].sort()
        prev = sys.maxsize
        seqlen = 1
        while suit[s]:
            r = suit[s].pop()
            if r == prev:
                continue
            if r == prev-1:
                seqlen += 1
                if max_seqlen < seqlen:
                    max_seqlen = seqlen
            else:
                seqlen = 1
            prev = r

    if max_seqlen > 1:
        sys.stdout.write(f'{max_seqlen}\n')
    else:
        sys.stdout.write('0\n')
