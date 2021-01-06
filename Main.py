from collections import Counter

c = Counter(input().upper())
mc = c.most_common(2)

print('?' if (len(mc) == 2 and mc[0][1] == mc[1][1]) else mc[0][0])