def solution():
    N = int(input())

    diagonal_to_left = set()
    diagonal_to_right = set()
    vertical = set()

    def n_queens(depth):
        answer = 0
        if depth == N-1:
            for x in range(N):
                if (x in vertical) or (depth+x in diagonal_to_left) or (depth-x in diagonal_to_right):
                    continue
                answer += 1
        elif depth == 0:
            for x in range(N):
                vertical.add(x)
                diagonal_to_left.add(x)
                diagonal_to_right.add(-x)
                answer += n_queens(depth+1)
                vertical.remove(x)
                diagonal_to_left.remove(x)
                diagonal_to_right.remove(-x)
        else:
            for x in range(N):
                if (x in vertical) or (depth+x in diagonal_to_left) or (depth-x in diagonal_to_right):
                    continue
                vertical.add(x)
                diagonal_to_left.add(depth+x)
                diagonal_to_right.add(depth-x)
                answer += n_queens(depth+1)
                vertical.remove(x)
                diagonal_to_left.remove(depth+x)
                diagonal_to_right.remove(depth-x)
        return answer

    print(n_queens(0))


if __name__ == "__main__":
    solution()
