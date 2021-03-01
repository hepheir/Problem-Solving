import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

pi = [0] * len(P) # 실패 함수

# 실패 함수 초기화
j = 0
for i in range(1, len(P)):
    while (j > 0) and (P[i] != P[j]):
        j = pi[j-1]
    if (P[i] == P[j]):
        j += 1
        pi[i] = j

# KMP 시작
t_idx = 0
p_idx = 0

found = []

while t_idx < len(T):
    while (p_idx > 0) and (T[t_idx] != P[p_idx]):
        p_idx = pi[p_idx-1]
    if T[t_idx] == P[p_idx]:
        if (p_idx == len(P)-1):
            found.append(t_idx-len(P)+1+1)
            p_idx = pi[p_idx]
        else:
            p_idx += 1
    t_idx += 1

print(len(found))
print(' '.join(map(str,found)))