import collections
import sys

cards = collections.defaultdict(lambda: 0)

N = int(sys.stdin.readline())
for x in map(int, sys.stdin.readline().split()):
    cards[x] += 1

M = int(sys.stdin.readline())
print(' '.join(str(cards[q]) for q in map(int, sys.stdin.readline().split())))