# 내 코드에서 반례 찾는 스크립트

import subprocess
import os
import sys
import functools

def sys_args(idx, prompt):
    return sys.argv[idx+1] if len(sys.argv) >= idx+2 else input(prompt)

################################################################################
# 문제에 따라 아래 값을 수정하여 사용
################################################################################

@functools.cache
def get_problem_path() -> os.PathLike:
    return os.path.join('problem', str(PROBLEM_ID))

def get_data_path(path:os.PathLike='data') -> os.PathLike:
    return os.path.join(get_problem_path(), path)

def get_source_path(path:os.PathLike='.py') -> os.PathLike:
    return os.path.join(get_problem_path(), path)

def data_generator():
    for n in range(1, 50001):
        yield str(n)+'\n'

PROBLEM_ID = int(sys_args(0, '문제 번호: '))
CORRECT_CODE = get_source_path(sys_args(1, '맞은 코드 파일: '))
WRONG_CODE = get_source_path(sys_args(2, '틀린 코드 파일: '))

################################################################################

TMP_STDOUT = 'tmp.stdout'
DEFAULT_TIMEOUT = 10

data_number, current_case, total_cases = 1, 1, 50000
print('[INFO] 데이터 셋 생성을 시작합니다.')
for data_in_content in data_generator():
    print(f'[INFO] {current_case}/{total_cases}', end='\r')
    data_in_path = os.path.join(get_data_path(), 'hepheir', f'{data_number}.in')
    data_out_path = os.path.join(get_data_path(), 'hepheir', f'{data_number}.out')
    if not os.path.exists(os.path.dirname(data_in_path)):
        os.makedirs(os.path.dirname(data_in_path))
    with open(data_in_path, 'w') as f:
        f.write(data_in_content)
    try:
        subprocess.run(f'''python3 -c "import py_compile; py_compile.compile(r'{CORRECT_CODE}')"''')
        subprocess.run(f'''python3 "{CORRECT_CODE}"''',
                        stdin=open(data_in_path,'r'),
                        stdout=open(data_out_path, 'w'))
        subprocess.run(f'''python3 -c "import py_compile; py_compile.compile(r'{WRONG_CODE}')"''')
        subprocess.run(f'''python3 "{WRONG_CODE}"''',
                        stdin=open(data_in_path,'r'),
                        stdout=open(TMP_STDOUT, 'w'),
                        check=True,
                        timeout=DEFAULT_TIMEOUT)
        with open(data_out_path, 'r') as ans_stdout, open(TMP_STDOUT, 'r') as usr_stdout:
            ans = ans_stdout.read().rstrip()
            usr = usr_stdout.read().rstrip()
            if ans != usr:
                raise ValueError()
    except:
        print('[INFO] 반례를 찾았습니다.')
        data_number += 1
    current_case += 1
print('[INFO] 데이터 셋 생성 종료.')
os.remove(TMP_STDOUT)