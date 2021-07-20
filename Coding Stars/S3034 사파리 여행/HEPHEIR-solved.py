def solve(total_gems, diff):
    half = (total_gems - diff) / 2
    hasDecimalPoints = bool(half - int(half))
    if (half < 0) or hasDecimalPoints:
        print('impossible')
    else:
        big_pile = int(half + diff)
        small_pile = int(half)
        print(big_pile, small_pile)

if __name__ == '__main__':
    # TESTCASES = int(input())
    # for t in range(TESTCASES):
    TOTAL_GEMS, DIFF = map(int, input().split())
    solve(TOTAL_GEMS, DIFF)
