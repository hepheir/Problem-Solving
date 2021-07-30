import collections
import sys

for t in range(int(sys.stdin.readline())):
    clothes = collections.defaultdict(list)
    for n in range(int(sys.stdin.readline())):
        name, category = sys.stdin.readline().rstrip().split()
        clothes[category].append(name)
    ans = 1
    for category, names in clothes.items():
        ans *= len(names)+1 # 입거나 안입거나
    sys.stdout.write(str(ans-1)+'\n')