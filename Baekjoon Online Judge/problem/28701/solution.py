N = int(input())

sum_pow_1 = 0
sum_pow_3 = 0

for x in range(1, N+1):
    sum_pow_1 += x
    sum_pow_3 += x*x*x

print(sum_pow_1)
print(sum_pow_1 * sum_pow_1)
print(sum_pow_3)
