from os import listdir
from sys import maxsize
from typing import List, Set

from boj import BOJProblem


def main():
    file_path = 'Baekjoon Online Judge/README.md'
    dir_name = 'Baekjoon Online Judge/problem/'

    # 누락된 문제 번호를 찾고, 표가 위치한 행 번호 범위를 지정

    table_start = maxsize
    table_end = 0

    table_numbers: Set[str] = set()
    dir_numbers: Set[str] = set()

    raw_content: List[str] = []
    new_content: List[str] = []

    with open(file_path, 'r', encoding='utf-8') as file_in:
        raw_content = file_in.readlines()

    for l_no, line in enumerate(raw_content):
        try:
            assert line.startswith('|')
            cells = list(map(lambda data: data.strip(), line.split('|')[1:-1]))
            int(cells[0])  # 타겟이 아니면 여기서 에러가 날 것.

            table_start = min(l_no, table_start)
            table_end = max(l_no+1, table_end)
            table_numbers.add(cells[0])

            new_line = ' | '.join(cells).strip() + '\n'

        except:
            new_line = line

        finally:
            new_content.append(new_line)

    for dir_name in listdir(dir_name):
        dir_numbers.add(dir_name)

    missing_numbers = (table_numbers - dir_numbers)
    unnecessary_numbers = (dir_numbers - table_numbers)

    # 표에 있지만 실제로는 없는 번호들 제거

    raw_table_body = raw_content[table_start:table_end]
    new_table_body = []

    for line in raw_table_body:
        cells = list(map(lambda data: data.strip(), line.split('|')[1:-1]))

        if cells[0] not in unnecessary_numbers:
            new_table_body.append(line)

    # 누락된 문제 번호들을 표에 삽입

    for number in missing_numbers:
        problem = BOJProblem(int(number))
        cells = [problem.id, '', '', problem.title]
        new_line = ' | '.join(map(str, cells)).strip() + '\n'

        new_table_body.append(new_line)

    # 하이퍼링크를 채우고 정렬

    for l_no in range(len(new_table_body)):
        line = new_table_body[l_no]

        cells = list(map(lambda data: data.strip(), line.split('|')[1:-1]))
        cells[1] = f'[📁](/Baekjoon%20Online%20Judge/problem/{cells[0]})'

        new_line = '| '+' | '.join(cells) + ' |\n'
        new_table_body[l_no] = new_line

    new_table_body.sort(key=lambda x: int(x.split('|')[1]))
    new_content = raw_content[:table_start] + new_table_body + raw_content[table_end:]

    with open(file_path, 'w', encoding='utf-8') as file_out:
        file_out.writelines(new_content)


if __name__ == '__main__':
    main()
