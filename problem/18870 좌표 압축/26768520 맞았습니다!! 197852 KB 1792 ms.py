import sys

N = int(sys.stdin.readline())

tmp_list = list(map(int, sys.stdin.readline().split()))
tmp_dict = dict()

for idx, num in enumerate(sorted(set(tmp_list))):
    tmp_dict[num] = idx

sys.stdout.write(' '.join(map(lambda x: str(tmp_dict[x]), tmp_list)))