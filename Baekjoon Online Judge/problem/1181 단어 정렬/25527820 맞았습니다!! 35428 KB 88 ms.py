from sys import stdin

data = list(map(lambda x:x.rstrip(),set(stdin.readlines()[1:])))
data.sort()
data.sort(key=len)
print('\n'.join(data))