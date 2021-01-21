from sys import stdin

N = int(stdin.readline())
data = list(map(lambda x:x.rstrip(),set(stdin.readlines())))
data.sort()
data.sort(key=lambda x:len(x))
print('\n'.join(data))