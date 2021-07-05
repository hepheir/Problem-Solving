from sys import maxsize


def solution(grid):
    width = len(grid[0])
    height = len(grid)
    dp = [[maxsize]*width for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if y == 0 and x == 0:
                dp[y][x] = grid[y][x]
                continue
            if y > 0:
                dp[y][x] = min(dp[y][x], grid[y][x] + dp[y-1][x])
            if x > 0:
                dp[y][x] = min(dp[y][x], grid[y][x] + dp[y][x-1])

    return dp[height-1][width-1]
