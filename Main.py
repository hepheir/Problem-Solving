from collections import defaultdict

alphabet_positions = defaultdict(lambda: -1)

for idx, val in enumerate(input()):
    if alphabet_positions[val] == -1:
        alphabet_positions[val] = idx

for char in 'abcdefghijklmnopqrstuvwxyz':
    print(alphabet_positions[char], end=' ')