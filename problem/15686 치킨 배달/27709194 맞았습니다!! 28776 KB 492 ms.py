import itertools
import sys

EMPTY = '0'
HOUSE = '1'
CHICKEN = '2'

def manhattan_dist(x0, y0, x1, y1):
    return abs(x0-x1) + abs(y0-y1)

N, M = map(int, sys.stdin.readline().split())
MAP = [sys.stdin.readline().split() for n in range(N)]

chickens = []
houses = []

for r in range(N):
    for c in range(N):
        if MAP[r][c] == CHICKEN:
            chickens.append((r,c))
        elif MAP[r][c] == HOUSE:
            houses.append((r,c))

chicken_dist = [[0]*len(chickens) for h in range(len(houses))]

for house_idx, house_pos in enumerate(houses):
    for chicken_idx, chicken_pos in enumerate(chickens):
        chicken_dist[house_idx][chicken_idx] = manhattan_dist(*house_pos, *chicken_pos)

answer = sys.maxsize
for selected_chickens in itertools.combinations(range(len(chickens)), M):
    city_chicken_dist = 0
    for house_idx in range(len(houses)):
        house_chicken_dist = sys.maxsize
        for chicken_idx in selected_chickens:
            house_chicken_dist = min(chicken_dist[house_idx][chicken_idx], house_chicken_dist)
        city_chicken_dist += house_chicken_dist
    answer = min(city_chicken_dist, answer)

print(answer)