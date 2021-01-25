import subprocess
import os
import glob

def get_problem_id(file:os.PathLike)->int:
    return int(os.path.split(file)[1])

def get_last_commit_message(file:os.PathLike)->str:
    buf = '.tmp.buffer'
    msg = ''
    with open(buf, 'w') as buffer:
        subprocess.run(f'git log --pretty=format:"%s"', stdout=buffer)
    with open(buf, 'r') as buffer:
        msg = buffer.read()
    os.remove(buf)
    return msg

def move_file(from:os.PathLike, to:os.PathLike, commit_msg:str='')->None:
    subprocess.run(f'git mv {from} {to}')
    subprocess.run(f'git commit -m "{commit_msg}"')

for file in glob.glob('**/*.py'):
    pid = get_problem_id(file)
    msg = get_last_commit_message(file)+' [mv]'
    mto = os.path.join(file)
    move_file(file, mto, msg)