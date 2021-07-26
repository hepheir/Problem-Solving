from sys import stdin


def solution():
    counter = [0] * 10001

    N = int(stdin.readline())
    for _ in range(N):
        n = int(stdin.readline())
        counter[n] += 1

    for n in range(1, 10001):
        print(f'{n}\n'*counter[n], end='')


if __name__ == '__main__':
    solution()
