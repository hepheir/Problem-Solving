import sys

S = set()
ans = list()

for t in range(int(sys.stdin.readline())):
    arg, *val = sys.stdin.readline().rstrip().split()

    # S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if arg == 'add':
        S.add(val[0])
    # S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif arg == 'remove':
        S.discard(val[0])
    # S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif arg == 'check':
        print('1' if (val[0] in S) else '0')
    # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif arg == 'toggle':
        S.remove(val[0]) if (val[0] in S) else S.add(val[0])
    # S를 {1, 2, ..., 20} 으로 바꾼다.
    elif arg == 'all':
        S = set(map(str, range(1, 21)))
    # S를 공집합으로 바꾼다. 
    elif arg == 'empty':
        S = set()

print('\n'.join(ans))