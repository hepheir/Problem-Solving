N, r, c = map(int, input().split())
answer = 0
size = 1<<N
x, y = 0, 0
while size > 1:
    size >>= 1
    skipped = 0
    if (c >= x+size):
        skipped += 1
        x += size
    if (r >= y+size):
        skipped += 2
        y += size
    answer += (size**2)*skipped
print(answer)