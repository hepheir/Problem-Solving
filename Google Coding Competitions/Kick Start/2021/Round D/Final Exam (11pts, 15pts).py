from sys import stdin
from collections import defaultdict


def main():
    testcases = int(stdin.readline())
    for t in range(1, testcases+1):
        N, M = map(int, stdin.readline().split())
        A = []
        B = []
        for n in range(N):
            a, b = map(int, stdin.readline().split())
            A.append(a)
            B.append(b)
        S = list(map(int, stdin.readline().split()))
        answer = solve(N, M, A, B, S)
        print(f"Case #{t}: {' '.join(answer)}")



def solve(N, M, A, B, S):
    problem_sets = list(zip(A, B))
    problem_sets.sort(lambda x: (x[1], x[0]))

    students = list(zip(S, range(M)))
    students.sort()

    for skill, idx in students:

        pass

    for student_num, skill in enumerate(S):
        for problem_num, problem_set in enumerate(problem_sets):
            if problem_set[1] <= skill:
                choosable_problems[student_num].append(problem_num)




if __name__ == "__main__":
    main()