def solve():
    X = int(input())
    answer = 0
    for i in range(8):
        if (X & (1 << i)):
            answer += 1
    return answer

print(solve())