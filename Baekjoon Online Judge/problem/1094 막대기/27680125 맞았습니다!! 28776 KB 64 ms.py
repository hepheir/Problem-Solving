def solve():
    X = int(input())
    answer = 0
    for b in bin(X)[2:]:
        if b == '1':
            answer += 1
    return answer

print(solve())