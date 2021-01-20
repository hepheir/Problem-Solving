def solve(recursion, numbers, start=0, chosen=[]):
    if recursion:
        for i in range(start, len(numbers)):
            chosen.append(str(numbers[i]))
            solve(recursion-1, numbers, i, chosen)
            chosen.pop()
    else:
        print(' '.join(chosen))

N, M = map(int, input().split())
numbers = list(range(1,N+1))

solve(M, numbers)