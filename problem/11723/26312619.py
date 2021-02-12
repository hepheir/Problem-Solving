import sys

BIN_ONE = 0b00000000000000000001
BIN_ZRO = 0b00000000000000000000

SET = BIN_ZRO

for t in range(int(sys.stdin.readline())):
    arg, *val = sys.stdin.readline().rstrip().split()
    bitmast = BIN_ONE << (int(val[0])-1) if val else BIN_ZRO
    # S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if arg == 'add':
        SET |= bitmast
    # S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif arg == 'remove':
        SET &= ~bitmast
    # S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif arg == 'check':
        sys.stdout.write('1\n' if (SET & bitmast) else '0\n')
    # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif arg == 'toggle':
        SET ^= bitmast
    # S를 {1, 2, ..., 20} 으로 바꾼다.
    elif arg == 'all':
        SET = ~bitmast
    # S를 공집합으로 바꾼다. 
    elif arg == 'empty':
        SET = bitmast