import os
import shutil
import subprocess

CORRECT_FILE = os.path.join('problem', '9019 DSLR', '27579162 맞았습니다!! 231544 KB 6156 ms.py.py')
COMPARE_FILE = os.path.join('problem', '9019 DSLR', '.py')

SAVE_DATA_AT = os.path.join('problem', '9019 DSLR', 'data', 'hepheir', 'auto')

TMP_STDIN = '.boj\\temp\\stdin.txt'
TMP_STDOUT_CORRECT = '.boj\\temp\\stdout_correct.txt'
TMP_STDOUT_COMPARE = '.boj\\temp\\stdout_compare.txt'


def D(n):
    return (n << 1) % 10000

def S(n):
    return 9999 if( n == 0) else n-1

def L(n):
    return (n * 10 + n // 1000) % 10000

def R(n):
    return ((n % 10) * 1000) + (n // 10)


STR2FUNC = {
    'D': D,
    'S': S,
    'L': L,
    'R': R,
}


def verdict(A, B, answer:str, submit:str):
    n = A
    for c in submit:
        n = STR2FUNC[c](n)
    return (n == B) and (len(answer) == len(submit))


for A in range(10000):
    for B in range(10000):
        with open(TMP_STDIN, 'w') as stdin:
            stdin.write('1\n')
            stdin.write(f'{A} {B}\n')
        with open(TMP_STDIN, 'r') as stdin,\
             open(TMP_STDOUT_CORRECT, 'w') as stdout_cor:
            subprocess.run(['python', CORRECT_FILE], stdin=stdin, stdout=stdout_cor)
        with open(TMP_STDIN, 'r') as stdin,\
             open(TMP_STDOUT_COMPARE, 'w') as stdout_cmp:
            subprocess.run(['python', COMPARE_FILE], stdin=stdin, stdout=stdout_cmp)
        with open(TMP_STDOUT_CORRECT, 'r') as stdout_cor,\
             open(TMP_STDOUT_COMPARE, 'r') as stdout_cmp:

            if not verdict(A, B, stdout_cor.read().rstrip(), stdout_cmp.read().rstrip()):
                shutil.copy(TMP_STDIN, os.path.join(SAVE_DATA_AT, f'{A} {B}.in'))
                shutil.copy(TMP_STDOUT_CORRECT, os.path.join(SAVE_DATA_AT, f'{A} {B}.out'))
                print(f'[WA] {A} {B}')
                continue
        # print(f'[AC] {A} {B}')
