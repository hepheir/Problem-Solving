"""
문제 폴더내에 있는 파이썬 코드에 대하여
간단한 채점을 시행하여 실행 시간과 채점 결과를 보여줍니다.

사용법: simple-python-judge.py [문제번호] [파일이름]
    - 문제번호: 생략시 콘솔에서 입력 받는 prompt가 나옴
    - 파일이름: 생략시 기본 값은 ".py"
"""

import subprocess
import os
import glob
import sys
import time
import typing

DEFAULT_TIMEOUT = 10
TMP_STDOUT = 'tmp.stdout'
BAR_SIZE = 48

################################################################################
# 파일 폴더 패턴에 따라 아래 함수를 수정하여 사용
################################################################################

def get_problem_path(pid:int) -> os.PathLike:
    return os.path.join('problem', str(pid))

################################################################################

def judge_brief(verdict:str='', took:float=0, data_in_path:os.PathLike='', end='\n'):
    data = [
        f'{verdict:10s}',
        f'{took:7.0f} ms' if took is not None else ' '*10,
        data_in_path,
    ]
    print('[INFO] '+'\t'.join(data), end=end)

def judge_problem(
        source_file:os.PathLike,
        input_files:typing.List[os.PathLike],
        output_files:typing.List[os.PathLike]
    ):
    for data_in, data_out in zip(input_files, output_files):
        with open(TMP_STDOUT, 'w') as stdout:
            judge_brief(verdict='채점중...', data_in_path=data_in, end='\r')
            verdict = ''
            took = None
            try:
                time_start = time.time()
                subprocess.run(f'''python3 -c "import py_compile; py_compile.compile(r'{source_file}')"''')
                subprocess.run(f'''python3 "{source_file}"''',
                                stdin=open(data_in,'r'),
                                stdout=stdout,
                                timeout=DEFAULT_TIMEOUT,
                                check=True)
                time_end = time.time()
                took =(time_end-time_start) * 1000
                with open(data_out, 'r') as ans_stdout, open(TMP_STDOUT, 'r') as usr_stdout:
                    ans = ans_stdout.read().rstrip()
                    usr = usr_stdout.read().rstrip()
                    if ans == usr:
                        verdict = '맞았습니다!!'
                    elif not usr:
                        verdict = '출력 없음'
                    else:
                        verdict = '틀렸습니다'
            except subprocess.TimeoutExpired:
                verdict = '시간 초과'
            except subprocess.CalledProcessError:
                verdict = '런타임 에러'
            except MemoryError: # TODO
                verdict = '메모리 초과'
            except BaseException as err:
                print(err)
            finally:
                judge_brief(verdict, took, data_in)
    print('[INFO] '+'='*BAR_SIZE)
    print('[INFO] 채점 완료')
    os.remove(TMP_STDOUT)

if __name__ == '__main__':
    pid = int(sys.argv[1] if len(sys.argv) >= 2 else input('[INFO] 문제 번호: '))
    problem_path = get_problem_path(pid)
    source_path = os.path.join(problem_path, sys.argv[2] if len(sys.argv) >= 3 else '.py')
    if not os.path.exists(source_path):
        print(f'[INFO] 소스 파일을 발견하지 못하였습니다. ["{source_path}" does not exist]')
        exit(1)
    else:
        print('[INFO] '+'='*BAR_SIZE)
        print(f'[INFO] 선택된 파일: {source_path}')
        print('[INFO] '+'='*BAR_SIZE)
    data_path = os.path.join(problem_path, 'data')
    data_in_list = glob.glob(os.path.join(data_path, '**','*.in'), recursive=True)
    data_out_list = glob.glob(os.path.join(data_path, '**','*.out'), recursive=True)
    judge_problem(source_path, data_in_list, data_out_list)