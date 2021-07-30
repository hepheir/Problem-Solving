A, B, V = map(int, input().split())
days, left = divmod(V-B, A-B)
if left:
    days += 1
print(days)