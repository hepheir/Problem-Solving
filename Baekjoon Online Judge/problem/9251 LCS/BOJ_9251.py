def solution():
    str1 = input()
    str2 = input()

    dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    answer = dp[len(str1)-1][len(str2)-1]

    print(answer)


if __name__ == '__main__':
    solution()
