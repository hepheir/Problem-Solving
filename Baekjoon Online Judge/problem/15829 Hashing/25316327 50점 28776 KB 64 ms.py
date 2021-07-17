R = 31
MOD = 1234567891

def h(c, i):
    # 나머지 연산의 분배법칙
    # * a는 최대 26으로 MOD보다 작아 a자체가
    #   나머지 값과 같으므로 그냥 사용.
    return (ord(c)-ord('a')+1) * pow(R, i, MOD) % MOD

input() # not used
print(sum([h(c,i) for i,c in enumerate(input())]))