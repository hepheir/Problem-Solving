import sys

N, M = map(int, sys.stdin.readline().split())
PAPER = [[*map(int, sys.stdin.readline().split())] for n in range(N)]

def get_score(matrix, width, height, tetromino):
    tetromino_width = max([t[0] for t in tetromino])
    tetromino_height = max([t[1] for t in tetromino])
    if (tetromino_width < width) and (tetromino_height < height):
        return sum([matrix[y][x] for x, y in tetromino])
    else:
        return 0

def get_max_possible_score(matrix, x, y, width, height):
    return max([
        get_score(matrix, width, height, [
            (x, y), (x+1, y), (x+2, y), (x+3, y),
        ]),
        get_score(matrix, width, height, [
            (x, y  ),
            (x, y+1),
            (x, y+2),
            (x, y+3),
        ]),
        get_score(matrix, width, height, [
            (x, y  ), (x+1, y  ),
            (x, y+1), (x+1, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y  ), (x+1, y  ),
            (x, y+1), (x+1, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y  ),
            (x, y+1),
            (x, y+2), (x+1, y+2),
        ]),
        get_score(matrix, width, height, [
                      (x+1, y  ),
                      (x+1, y+1),
            (x, y+2), (x+1, y+2),
        ]),
        get_score(matrix, width, height, [
            (x, y), (x+1, y  ),
                    (x+1, y+1),
                    (x+1, y+2),
        ]),
        get_score(matrix, width, height, [
            (x, y  ), (x+1, y  ),
            (x, y+1),
            (x, y+2),
        ]),
        get_score(matrix, width, height, [
            (x, y), (x+1, y), (x+2, y  ),
                              (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y  ), (x+1, y), (x+2, y),
            (x, y+1),
        ]),
        get_score(matrix, width, height, [
                                  (x+2, y  ),
            (x, y+1), (x+1, y+1), (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y  ),
            (x, y+1), (x+1, y+1), (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y), (x+1, y), (x+2, y  ),
                              (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y  ),
            (x, y+1), (x+1, y+1),
                      (x+1, y+2),
        ]),
        get_score(matrix, width, height, [
                      (x+1, y  ),
            (x, y+1), (x+1, y+1),
            (x, y+2),
        ]),
        get_score(matrix, width, height, [
            (x, y), (x+1, y  ),
                    (x+1, y+1), (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
                      (x+1, y  ), (x+2, y),
            (x+1, y), (x+1, y+1),
        ]),
        get_score(matrix, width, height, [
            (x, y), (x+1, y  ), (x+2, y),
                    (x+1, y+1),
        ]),
        get_score(matrix, width, height, [
                      (x+1, y  ),
            (x, y+1), (x+1, y+1), (x+2, y+1),
        ]),
        get_score(matrix, width, height, [
                    (x+1, y  ),
            (x, y), (x+1, y+1),
                    (x+1, y+2),
        ]),
        get_score(matrix, width, height, [
            (x, y  ),
            (x, y+1), (x+1, y+1),
            (x, y+2),
        ]),
    ])

answer = 0
for y in range(N):
    for x in range(M):
        answer = max(get_max_possible_score(PAPER, x, y, M, N), answer)

print(answer)