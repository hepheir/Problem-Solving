def get_depth(n):
    start = 1
    level = 1
    while start < n:
        start += 6*level
        level += 1
    return level

N = int(input())
print(get_depth(N))