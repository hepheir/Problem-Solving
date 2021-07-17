import sys
sys.setrecursionlimit(10**6)

MAX_LEN = 2**31-1

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for k in range(K)]

def get_cases(len):
    retval = 0
    for line in lines:
        retval += line // len
    return retval

def bin_search(start, end, value):
    mid = (start+end)//2
    cases = get_cases(mid)
    if cases == value:
        return mid
    elif cases > value:
        return bin_search(mid+1, end, value)
    else:
        return bin_search(start, mid-1, value)

ans = bin_search(1, max(lines), N)

while get_cases(ans+1) == N:
    ans += 1

print(ans)