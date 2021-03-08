import os
import subprocess

DATASET_NUMBER = 1

DIRNAME = os.path.join(os.path.dirname(__file__), 'worstcase')
RELIABLE_SOURCE = 'problem/7576 토마토/27069390 시간 초과.py'

INPUT_FILENAME = os.path.join(DIRNAME, f'{DATASET_NUMBER}.in')
OUTPUT_FILENAME = os.path.join(DIRNAME, f'{DATASET_NUMBER}.out')

# input file generator
with open(INPUT_FILENAME, 'w') as input_file:
    input_file.write('1000 1000\n')
    for x in range(1000):
        input_file.write(' '.join(['1']*1000)+'\n')

subprocess.run(
    args=['python', RELIABLE_SOURCE],
    stdin=open(INPUT_FILENAME, 'r'),
    stdout=open(OUTPUT_FILENAME, 'w'),
    check=True)
