from sys import stdin

def cmp_dungchi(x, y):
    if (x[0] > y[0]) and (x[1] > y[1]):
        return 1 # x > y
    if (x[0] < y[0]) and (x[1] < y[1]):
        return -1 # x < y
    return 0 # can't compare

data = [tuple(map(int, l.split())) for l in stdin.readlines()[1:]]

for i in range(len(data)):
    rank = 1
    for j in range(len(data)):
        if i == j: continue
        if cmp_dungchi(data[i], data[j]) == -1:
            rank += 1
    print(rank, end=' ')