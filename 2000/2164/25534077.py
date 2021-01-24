import collections

deque = collections.deque(range(1, int(input())+1))

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])