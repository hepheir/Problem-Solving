"""
문제 폴더내에 있는 파이썬 코드에 대하여
간단한 채점을 시행하여 실행 시간과 채점 결과를 보여줍니다.

사용법:simple-python-judge.py [문제번호] [파일이름]
    - 문제번호:생략시 콘솔에서 입력 받는 prompt가 나옴
    - 파일이름:생략시 기본 값은 ".py"
"""

import argparse
import glob
import os
import shutil
import subprocess
import time
import typing

TMP_PATH = 'tmp'


class Python3:
    BACKUP_PATH = os.path.join(TMP_PATH, 'tmp.py')

    @classmethod
    def compile(cls, src:os.PathLike):
        shutil.copyfile(src, cls.BACKUP_PATH)
        subprocess.run([
                'python3',
                '-c',
                f'"import py_compile; py_compile.compile(r\'{cls.BACKUP_PATH}\')"'
            ])

    @classmethod
    def run(cls, src:os.PathLike, stdin:os.PathLike, stdout:os.PathLike, timeout:float = 10):
        subprocess.run(f'''python3 "{src}"''',
                       stdin=open(stdin, 'r'),
                       stdout=open(stdout, 'w'),
                       timeout=timeout,
                       check=True)


class Cpp:
    COMPILER_PATH = 'c:\\MinGW\\bin\\g++.exe'
    BACKUP_PATH = os.path.join(TMP_PATH, 'tmp.cpp')
    OUTPUT_PATH = os.path.join(TMP_PATH, 'tmp.exe')

    @classmethod
    def compile(cls, src:os.PathLike):
        shutil.copyfile(src, cls.BACKUP_PATH)
        subprocess.run([
                cls.COMPILER_PATH,
                "-g",
                cls.BACKUP_PATH,
                "-o",
                cls.OUTPUT_PATH
            ])

    @classmethod
    def run(cls, src:os.PathLike, stdin:os.PathLike, stdout:os.PathLike, timeout:float=5):
        subprocess.run(
            cls.OUTPUT_PATH,
            stdin=open(stdin, 'r'),
            stdout=open(stdout, 'w'),
            timeout=timeout,
            check=True
        )


class Log:
    PREFIX = '[INFO] '
    BAR_SIZE = 56
    CELL_WIDTH = 10

    @classmethod
    def info(cls, *args, **kwargs):
        print(cls.PREFIX+'\t'.join(map(lambda x:f'{str(x):{cls.CELL_WIDTH}s}', args)), **kwargs)

    @classmethod
    def bar(cls):
        print(cls.PREFIX + '='*cls.BAR_SIZE)


class Judge:
    TMP_STDOUT = os.path.join(TMP_PATH, 'tmp.stdout')

    @classmethod
    def detect_language(cls, src):
        ext = os.path.splitext(src)[1]
        if not ext:
            ext = os.path.basename(src)
        if ext == '.py':
            return Python3
        if ext == '.cpp':
            return Cpp
        return None

    @classmethod
    def test(cls, src:os.PathLike, din:typing.List[os.PathLike], dout:typing.List[os.PathLike]):
        lang = cls.detect_language(src)
        for data_in, data_out in zip(din, dout):
            shorted_data_in = data_in.replace(os.path.commonpath([src, data_in]), '...')
            verdict = None
            took = None

            Log.info('채점 중...', shorted_data_in, end='\r')
            try:
                # Compile
                lang.compile(src)

                # Run & Check time
                time_start = time.time()

                lang.run(src, data_in, cls.TMP_STDOUT)
                
                time_end = time.time()
                took = (time_end-time_start) * 1000
                
                # Judge
                with open(data_out, 'r') as ans_stdout, open(cls.TMP_STDOUT, 'r') as usr_stdout:
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
            except BaseException as error:
                raise error # 알 수 없는 에러 (버그 제보 부탁)
            finally:
                brief_result = verdict if (verdict is not None) else ''
                brief_time = f'{took:7.0f} ms' if (took is not None) else ''
                brief_data = shorted_data_in
                Log.info(brief_result, brief_time, brief_data)
        # Fin.
        Log.bar()
        Log.info('채점 완료')


def check_required_path_exists(path:os.PathLike):
    if not os.path.exists(path):
        Log.info('경로를 찾지 못하였습니다.', path)
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
'''
:: Baekjoon Offline Judge ::

* 짭준 오프라인 저지.
  당신의 채점 결과를 예측해 드립니다.

''',
        usage='<source file> <dataset dir>'
    )
    parser.add_argument('src', help='작성한 소스코드의 경로')
    parser.add_argument('data', help='[.in .out]형식으로 저장된 데이터 셋이 들어있는 폴더 경로')

    args = parser.parse_args()
    
    Log.bar()
    Log.info('선택된 파일:', args.src)
    Log.bar()

    check_required_path_exists(args.src)
    check_required_path_exists(args.data)

    if not os.path.exists(TMP_PATH): os.makedirs(TMP_PATH)
    
    din = glob.glob(os.path.join(args.data, '**', '*.in'), recursive=True)
    dout = glob.glob(os.path.join(args.data, '**', '*.out'), recursive=True)

    Judge.test(args.src, din, dout)
