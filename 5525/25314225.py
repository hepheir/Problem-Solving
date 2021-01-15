n = int(input())
_ = input() # not used

found = 0
combo = 0
thresh = 1 + 2*n

pc = 'O' # previous character
for c in input():
    if pc == c:
        combo = 1 if c == 'I' else 0
    else:
        combo += 1
        if combo % 2 and combo >= thresh:
            found += 1
    pc = c

print(found)