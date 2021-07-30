from typing import List


def check_validation(stack: List[int], x: int) -> bool:
    """스택에 있는 그 어떤 말과도 대각선과 직선상에 있지 않으면 True를 반환.

    스택을 해석하는 방법은 다음과 같다:
        스택의 원소의 인덱스 번호: 행 번호
        스택의 원소의 값: 열 번호

        -> 해당 행, 열 좌표에는 퀸이 있다.
    """
    y = len(stack)
    for index, number in enumerate(stack):
        x_diff = abs(x-number)
        y_diff = abs(y-index)
        if x_diff == 0:
            return False
        if y_diff == x_diff:
            return False
    return True


def backtracking(stack: List[int], n: int):
    """백트래킹으로 퀸을 서로 공격할 수 없게 둘 수 있는 모든 경우를 구한다.

    특정 열에 말을 둘 수 있는지를 체크한 뒤,
    가능하다면 해당 열에 말을 두고(stack에다 push) 다음 열을 체크,
    불가능하다면 말을 치우고(stack에서 pop), 이전 행으로 돌아간다.
    """
    if len(stack) == n:
        return 1
    else:
        cases = 0
        for x in range(n):
            if check_validation(stack, x):
                stack.append(x)
                cases += backtracking(stack, n)
                stack.pop()
        return cases


def solution():
    N = int(input())

    stack = []
    answer = backtracking(stack, N)

    print(answer)


if __name__ == "__main__":
    solution()
