def solve(recursion, numbers, chosen=[]):
    if recursion:
        for i in numbers:
            if i not in chosen:
                chosen.append(i)
                solve(recursion-1, numbers, chosen)
                chosen.pop()
    else:
        print(' '.join(map(str, chosen)))

N, M = map(int, input().split())
numbers = list(sorted(set(map(int, input().split()))))

solve(M, numbers)