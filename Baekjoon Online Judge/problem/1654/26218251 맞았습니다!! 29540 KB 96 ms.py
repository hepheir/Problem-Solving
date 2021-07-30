import sys

K, N = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readlines()))


def get_cases(len):
    retval = 0
    for line in lines:
        retval += line // len
    return retval


def bin_search(start, end, value):
    ans = -1
    while start <= end:
        mid = (start+end)//2
        cases = get_cases(mid)
        if cases >= value:
            # 길이를 늘려봐야 함
            start = mid+1
            ans = mid
        elif cases < value:
            # 길이를 줄여봐야 함
            end = mid-1
    return ans


print(bin_search(1, max(lines), N))
