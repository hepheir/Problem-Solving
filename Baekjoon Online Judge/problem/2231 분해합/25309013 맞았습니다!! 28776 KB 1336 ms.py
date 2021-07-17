def digit_sum(x):
    return sum(map(int, str(x)))

n_str = input().strip()
n = int(n_str)

for x in range(n+1):
    if n == x + digit_sum(x):
        print(x)
        break
else:
    print(0)