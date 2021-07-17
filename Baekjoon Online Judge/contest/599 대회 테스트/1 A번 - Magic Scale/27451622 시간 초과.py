import collections

N = int(input())
K = int(input())
W = map(int, input().split())

deque = collections.deque(sorted(collections.Counter(W).most_common(), key=lambda x: x[0]))
memo = dict()

while deque:
    cur_num, cur_amount = deque.popleft()
    for a in range(1, cur_amount+1):
        new_dict = {}
        for cached_num in memo:
            new_number = cached_num + cur_num*a
            if new_number not in memo:
                new_dict[new_number] = memo[cached_num].copy()
                new_dict[new_number].append(cur_num)
        memo.update(new_dict)
    if cur_num not in memo:
        memo[cur_num] = [cur_num]

print('0:')

for num in sorted(memo):
    print(f'{num}: '+' '.join(map(str, memo[num])))
    if (K := K-1) <= 1:
        break
