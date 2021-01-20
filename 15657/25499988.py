def solve(recursion, numbers, start=0, chosen=[]):
    if recursion:
        for i in range(start, len(numbers)):
            chosen.append(numbers[i])
            solve(recursion-1, numbers, i, chosen)
            chosen.pop()
    else:
        print(' '.join(map(str, chosen)))

N, M = map(int, input().split())
numbers = list(sorted(set(map(int, input().split()))))

solve(M, numbers)