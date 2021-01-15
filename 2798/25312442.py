n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            sum_of_cards = card[i]+card[j]+card[k]
            if sum_of_cards <= m:
                ans = max(ans, sum_of_cards)
print(ans)