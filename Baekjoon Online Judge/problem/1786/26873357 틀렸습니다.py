import functools
import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

@functools.cache
def pi(x):
    mid = x//2
    for i in range(mid, -1, -1):
        for j in range(i):
            if P[j] != P[i-mid-1+j]:
                break
        else:
            return mid
    return 0

t_idx = 0
p_idx = 0

found = []

while t_idx < len(T):
    while (p_idx > 0) and (T[t_idx] != P[p_idx]):
        p_idx = pi(p_idx-1)
    if T[t_idx] == P[p_idx]:
        if (p_idx == len(P)-1):
            found.append(t_idx-len(P)+1+1)
            p_idx = pi(p_idx)
        else:
            p_idx += 1
    t_idx += 1

print(len(found))
print(' '.join(map(str,found)))