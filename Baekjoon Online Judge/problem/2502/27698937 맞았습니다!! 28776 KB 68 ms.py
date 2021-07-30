D, K = map(int, input().split())

fibo = [0,1]
for d in range(2, D+1):
    fibo.append(fibo[d-1]+fibo[d-2])

for a in range(1, K):
    b, r = divmod(K - fibo[D-2]*a, fibo[D-1])
    if r:
        continue
    print(a)
    print(b)
    break