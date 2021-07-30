import sys
import collections

N = int(sys.stdin.readline())

tmp_list = [0]*N
tmp_dict = collections.defaultdict(list)
for index, value in enumerate(map(int, sys.stdin.readline().split())):
    tmp_dict[value].append(index)

for compressed_coordinate, value in enumerate(sorted(tmp_dict)):
    for index in tmp_dict[value]:
        tmp_list[index] = compressed_coordinate

print(' '.join(map(str, tmp_list)))