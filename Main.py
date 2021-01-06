counter = dict()

for char in input().upper():
    if char not in counter:
        counter[char] = 0
    counter[char] += 1

sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)

if len(counter) > 1 and (counter[sorted_counter[0]] == counter[sorted_counter[1]]):
    print('?')
else:
    print(sorted_counter[0])