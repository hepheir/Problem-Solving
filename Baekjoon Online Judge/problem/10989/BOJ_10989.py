from sys import stdin, stdout


def solution():
    counter = [0] * 10001

    N = int(stdin.readline())
    for _ in range(N):
        n = int(stdin.readline())
        counter[n] += 1

    for n in range(1, 10001):
        for _ in range(counter[n]):
            stdout.write(str(n)+'\n')


if __name__ == '__main__':
    solution()
