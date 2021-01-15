R = 31
MOD = 1234567891

def h(c, i):
    a = ord(c)-ord('a')+1
    return a * (R**i) % MOD

input() # not used
print(sum([h(c,i) for i, c in enumerate(input())]))
