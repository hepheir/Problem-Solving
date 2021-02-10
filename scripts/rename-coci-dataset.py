'''
미래의 나에게,

이 스크립트를 COCI 데이터 셋이 있는 폴더에 넣고 실행하면 된다.
'''

import os
import glob

current_dir = os.path.dirname(__file__)

for file in glob.glob(os.path.join(current_dir, '*')):
    if file.endswith('.py') or 'boj' in file: continue
    data = os.path.basename(file).split('.')
    data[-1], data[-2] = data[-2], data[-1]
    data.insert(0, 'coci')
    newfile = os.path.join(current_dir, '.'.join(data))
    os.rename(file, newfile)
