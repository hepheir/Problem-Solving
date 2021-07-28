def LCS(X, Y, i, j):
    # https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4
    # LCS 함수의 정의 참조
    if i < 0 or j < 0:
        return 0
    if X[i] == Y[j]:
        return LCS(X, Y, i-1, j-1)+1
    else:
        return max(LCS(X, Y, i, j-1), LCS(X, Y, i-1, j))


def solution():
    str_long = input()
    str_short = input()

    print(LCS(str_long, str_short, len(str_long)-1, len(str_short)-1))


if __name__ == '__main__':
    solution()
