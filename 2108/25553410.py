from sys import stdin
from collections import Counter

numbers = [*map(int,stdin.readlines()[1:])]

# 산술평균
print(round(sum(numbers)/len(numbers)))

# 중앙값
numbers.sort()
print(numbers[len(numbers)//2])

# 최빈값
counter = Counter(numbers)
most_count = max(counter.most_common(), key=lambda x:x[1])[1]
most_numbers = [*sorted(num for num, cnt in counter.most_common() if cnt == most_count)]
if len(most_numbers) > 1:
    print(most_numbers[1])
else:
    print(most_numbers[0])

# 범위
print(max(numbers)-min(numbers))