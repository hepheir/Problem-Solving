from sys import stdin


def solution():
    n_students, *scores = map(int, stdin.readline().split())
    average_score = sum(scores) / n_students

    good_scores = list(filter(lambda score: score > average_score, scores))
    n_good_students = len(good_scores)

    rate = n_good_students / n_students
    print(f'{round(rate*100, ndigits=3):.3f}%')


if __name__ == "__main__":
    n_testcases = int(stdin.readline())
    for _ in range(n_testcases):
        solution()
