def solution(price, money, count):
    coeff = 0
    for c in range(1, count+1):
        coeff += c

    return max(0, coeff*price - money)