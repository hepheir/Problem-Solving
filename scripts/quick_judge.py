import subprocess
import os
import glob
import sys

DEFAULT_SOURCE = '.py'
DEFAULT_DATA = 'data'
DEFAULT_TIMEOUT = 10

TMP_STDOUT = 'tmp.stdout'
TMP_STDERR = 'tmp.stderr'

pid = int(sys.argv[1] if len(sys.argv) == 2 else input('문제 번호: '))

problem_path = os.path.join(str(pid//1000*1000), str(pid))
source = os.path.join(problem_path, DEFAULT_SOURCE)
data = os.path.join(problem_path, DEFAULT_DATA)

for data_in, data_out in zip(*map(lambda ext: glob.glob(os.path.join(data,'*'+ext)), ['.in', '.out'])):
    with open(TMP_STDOUT, 'w') as stdout, open(TMP_STDERR, 'w') as stderr:
        verdict = ''
        try:
            subprocess.run(f'''python3 -c "import py_compile; py_compile.compile(r'{source}')"''')
            subprocess.run(f'''python3 "{source}"''',
                            stdin=open(data_in,'r'),
                            stdout=stdout,
                            stderr=stderr,
                            timeout=DEFAULT_TIMEOUT)
            with open(TMP_STDERR, 'r') as usr_stderr:
                if usr_stderr.read():
                    verdict = '런타임 에러'
                else:
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
        finally:
            data_in = data_in.replace('\\', '/')
            print(f'{verdict:10s}\t{data_in}')

os.remove(TMP_STDOUT)
os.remove(TMP_STDERR)
    