from math import floor, log10


def d(n):
    ans = n
    while n > 0:
        base = 10**floor(log10(n))
        ans += n // base
        n %= base
    return ans


def main():
    is_self_number = [True] * 10001
    for n in range(10000, 0, -1):
        while is_self_number[n]:
            n = d(n)
            if n > 10000:
                break
            is_self_number[n] = False
    for n in filter(lambda x: is_self_number[x], range(1, 10001)):
        print(n)


if __name__ == '__main__':
    main()
