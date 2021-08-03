def solution(price, money, count):
    return max(0, sum(range(1, count+1))*price - money)