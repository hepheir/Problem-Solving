MAX_N:int = 100000

eratos = [True] * (MAX_N+1)
for i in range(int(MAX_N**0.5)+1): # sqrt(n) 까지 검사
    if i < 2:
        eratos[i] = False # 0, 1은 소수가 아님

    elif eratos[i]: # 이미 소수가 아니면 건너 뜀
        for j in range(2*i, MAX_N+1, i):
            # array[i]는 소수이므로 pass
            # 2i번 부터 i의 배수들을 모두 소수가 아닌 것으로 표시
            eratos[j] = False