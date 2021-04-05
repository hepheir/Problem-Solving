MAX_N = int(1e6)

INF = MAX_N+1
NAN = -1

COUNT = 0
PREV = 1


def backtrace(dp_arr, start):
    num = start
    while dp_arr[num][PREV] > NAN:
        yield num
        num = dp_arr[num][PREV]
    yield num


def solve():
    N = int(input())

    # [(횟수, 이전숫자)]
    dp = [(INF, NAN)] * (MAX_N+1)
    dp[1] = (0, NAN)

    for num in range(1, N+1):
        for next_num in [3*num, 2*num, num+1]:
            if (next_num <= MAX_N) and (dp[next_num][COUNT] > dp[num][COUNT]+1):
                dp[next_num] = (dp[num][COUNT]+1, num)

    print(dp[N][0]) # 횟수
    print(' '.join(map(str, backtrace(dp, N))))

solve()
