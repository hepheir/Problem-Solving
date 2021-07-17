import collections


def childs(y, x):
    if y > 0:
        yield y-1, x
    if y < 4:
        yield y+1, x
    if x > 0:
        yield y, x-1
    if x < 4:
        yield y, x+1


def dfs(place, y, x, py, px, dist=2):
    if dist < 0:
        return True
    if place[y][x] == 'X':
        return True
    if place[y][x] == 'P':
        if dist != 2 and not (py == y and px == x):
            return False
    for ny, nx in childs(y, x):
        if not dfs(place, ny, nx, y, x, dist-1):
            return False
    return True


def check_room(place) -> int:
    place = [list(line) for line in place]
    deque = collections.deque()
    count = 0
    for y in range(5):
        for x in range(5):
            if place[y][x] == 'P':
                deque.append((y, x, count))
                place[y][x] = count
                count += 1
    for _ in range(3): # depth == manhattan distance
        for _ in range(len(deque)): # width
            y, x, pid = deque.popleft()
            if (place[y][x] == 'X'):
                continue
            elif (place[y][x] == 'O') or (place[y][x] == pid):
                for ny, nx in childs(y, x):
                    deque.append((ny, nx, pid))
            else:
                return 0
    return 1



def solution(places):
    answer = [check_room(place) for place in places]
    return answer


print(solution([[
    "OOOOO",
    "OOOOO",
    "OOPXO",
    "OOXPO",
    "OOOOO"]]))
print(solution([[
    "OOOOO",
    "OOOOO",
    "OOPXO",
    "OOOPO",
    "OOOOO"]]))
print(solution([[
    "OOOOO",
    "OOOOO",
    "OOXOO",
    "OPXPO",
    "OOOOO"]]))
print(solution([[
    "PXPOO",
    "XPXOO",
    "PXPXO",
    "XPXPO",
    "OPOOO"]]))
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))