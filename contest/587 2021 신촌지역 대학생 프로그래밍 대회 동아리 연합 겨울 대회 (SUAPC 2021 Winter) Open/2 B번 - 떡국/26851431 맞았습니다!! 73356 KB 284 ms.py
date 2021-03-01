import collections
import sys

N = int(sys.stdin.readline())
counter = collections.Counter(map(int, sys.stdin.readline().split()))

print(max(counter.values()))