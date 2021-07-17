import sys

APPLE = -2
EMPTY = -1

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3

X = 0
Y = 1


def int_1to0(x):
    return int(x)-1


def next_pos(board, x, y):
    if board[y][x] == EAST:
        x += 1
    elif board[y][x] == SOUTH:
        y += 1
    elif board[y][x] == WEST:
        x -= 1
    elif board[y][x] == NORTH:
        y -= 1
    return x, y


def turn_left(board, x, y):
    board[y][x] -= 1
    board[y][x] %= 4


def turn_right(board, x, y):
    board[y][x] += 1
    board[y][x] %= 4


def is_snake(board, x, y):
    return board[y][x] >= 0


def is_inside_box(board, x, y):
    return (0 <= x < len(board)) and (0 <= y < len(board))


def move_if_movable(board, snake_head, snake_tail):
    hx, hy = next_pos(board, *snake_head)
    tx, ty = next_pos(board, *snake_tail)

    if not is_inside_box(board, hx, hy) or is_snake(board, hx, hy):
        return False

    direction = board[snake_head[Y]][snake_head[X]]
    eaten = board[hy][hx]

    snake_head[X], snake_head[Y] = hx, hy
    board[snake_head[Y]][snake_head[X]] = direction

    if eaten == APPLE:
        return True

    board[snake_tail[Y]][snake_tail[X]] = EMPTY
    snake_tail[X], snake_tail[Y] = tx, ty
    return True


def solve():
    board_size = int(sys.stdin.readline())  # N
    board = [[EMPTY]*(board_size) for _ in range(board_size)]
    time = 1
    snake_head = [0, 0]
    snake_tail = [0, 0]

    board[0][0] = EAST
    for _ in range(int(sys.stdin.readline())):  # K
        r, c = map(int_1to0, sys.stdin.readline().split())
        board[r][c] = APPLE

    for _ in range(int(sys.stdin.readline())):  # L
        args = sys.stdin.readline().split()
        X = int(args[0])
        C = args[1]

        for _ in range(time, X+1):
            if not move_if_movable(board, snake_head, snake_tail):
                return time
            time += 1

        if C == 'L':
            turn_left(board, *snake_head)
        else:
            turn_right(board, *snake_head)

    while move_if_movable(board, snake_head, snake_tail):
        time += 1

    return time


print(solve())
