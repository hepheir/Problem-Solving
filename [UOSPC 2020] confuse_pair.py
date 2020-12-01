S, T = input().split()
confused_pair = []

for a in range(2, 11):
  for b in range(2, 11):
    try:
      if int(S, base=a) == int(T, base=b):
        confused_pair.append((a, b))
    except:
      pass

print(len(confused_pair))
