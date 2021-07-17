def solve():
    A, B = map(int, input().split())
    count = 0
    while A <= B:
        if (A == B):
            return count+1

        elif (B % 10 == 1):
            B //= 10
            count += 1

        elif (B % 2 == 0):
            B //= 2
            count += 1

        else:
            break

    return '-1'

print(solve())