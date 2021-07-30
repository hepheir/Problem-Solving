from os import listdir

problems_in_dir = set()
problems_in_table = set(listdir('Baekjoon Online Judge\problem'))

with open('Baekjoon Online Judge\README.md', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if line.startswith('|'):
            args = line.split('|')
            if len(args) == 6:
                try:
                    problem_id = int(args[1].strip())
                    problem_id_str = str(problem_id)

                    problems_in_dir.add(problem_id_str)
                except Exception:
                    pass

print('표에 아직 작성되지 않음:')
print()
for diff in problems_in_dir-problems_in_table:
    print(diff)

print()
print()
print('표에는 있지만 폴더가 없음:')
for diff in problems_in_table-problems_in_dir:
    print(diff)
