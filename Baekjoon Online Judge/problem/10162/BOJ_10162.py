_Second = int

A: _Second = 300
B: _Second = 60
C: _Second = 10


def main():
    T = int(input())

    seconds: _Second = T
    count_a: int = 0
    count_b: int = 0
    count_c: int = 0

    count_a += seconds // A
    seconds %= A

    count_b += seconds // B
    seconds %= B

    count_c += seconds // C
    seconds %= C

    if seconds:
        print('-1')
    else:
        print(count_a, count_b, count_c)



if __name__ == '__main__':
    main()
