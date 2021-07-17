import sys


def solve():
    X, Y, S = sys.stdin.readline().rstrip().split()
    X, Y = map(int, (X, Y))
    # Get first known character
    for c in S:
        last_known_char = c
        if last_known_char != '?':
            break
    else:
        # All the characters are '?' == no cost
        return 0
    cost = 0
    for c in S:
        if c == '?':
            continue
        else:
            if (last_known_char != c):
                if (last_known_char == 'C'):
                    cost += X
                else:
                    cost += Y
            last_known_char = c
    return cost


T = int(sys.stdin.readline())
for t in range(1, T+1):
    print(f'Case #{t}: {solve()}')
