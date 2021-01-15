R = 31
MOD = 1234567891

def ctoi(c):
    return ord(c) - 96

def pow_generator(base, mod):
    buff = 1
    yield 1
    while True:
        buff = (buff * (base % mod)) % mod
        yield buff

input() # not used

ans = 0
for ai, ri in zip(map(ctoi, input()), pow_generator(R, MOD)):
    ans = (ans + ai*ri) % MOD

print(ans)