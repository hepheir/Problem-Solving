import collections
import sys

sys.stdin.readline()
counter = collections.Counter(map(lambda x:x.rstrip(), sys.stdin.readline().split()))

sys.stdin.readline()
print(' '.join(map(lambda x: str(counter[x.rstrip()]), sys.stdin.readline().split())))