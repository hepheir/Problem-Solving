from sys import stdin

counter = [0]*10001

for n in range(int(stdin.readline())):
    counter[int(stdin.readline())] += 1

for num, cnt in enumerate(counter):
    if cnt:
        print('\n'.join([str(num)]*cnt))