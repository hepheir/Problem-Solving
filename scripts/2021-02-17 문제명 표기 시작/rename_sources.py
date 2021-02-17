import os
from os.path import split
import sys
import subprocess
import glob

def last_commit_message(src: os.PathLike) -> str:
    BUFFER = 'tmp.txt'
    commit = ''
    src = src.replace('\\', '/')
    with open(BUFFER, 'wt', encoding='UTF8') as buffer:
        subprocess.run(f'git log --pretty=format:"%s" -- {src}', 
                        stdout=buffer,
                        check=True)
    with open(BUFFER, 'rt', encoding='UTF8') as buffer:
        commit = buffer.read()
    os.remove(BUFFER)
    return commit

for file in glob.glob('**/*.py', recursive=True):
    if 'problem' not in file:
        continue
    if len(os.path.basename(file).split()) > 1:
        continue
    now_problem_path = os.path.dirname(file)
    old_problem_path = os.path.dirname(file).split()[0]

    original_source = file.replace(now_problem_path, old_problem_path)
    result = ' '+last_commit_message(original_source).replace('\t', ' ')

    splitted_file = list(os.path.splitext(file))
    splitted_file.insert(1, result)
    new_file = ''.join(splitted_file)
    os.rename(file, new_file)