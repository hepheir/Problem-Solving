import glob
import os
import subprocess


class git:
    def last_commit_message(src: os.PathLike) -> str:
        BUFFER = 'tmp.txt'
        commit = ''
        with open(BUFFER, 'wt', encoding='UTF8') as buffer:
            subprocess.run(f'git log --pretty=format:"%s" {src}', 
                            stdout=buffer,
                            check=True)
        with open(BUFFER, 'rt', encoding='UTF8') as buffer:
            commit = buffer.read()
        os.remove(BUFFER)
        return commit

    def last_commit_hash(src: os.PathLike) -> str:
        BUFFER = 'tmp.txt'
        commit = ''
        with open(BUFFER, 'wt', encoding='UTF8') as buffer:
            subprocess.run(f'git log --pretty=format:"%H" {src}', 
                            stdout=buffer,
                            check=True)
        with open(BUFFER, 'rt', encoding='UTF8') as buffer:
            commit = buffer.read()
        os.remove(BUFFER)
        return commit

    def move(src: os.PathLike, dst: os.PathLike):
        subprocess.run(f'git mv {src} {dst}', check=True)
    
    def commit(commit):
        subprocess.run(f'git commit -m "{commit}"', check=True)
    
    def add(target):
        subprocess.run(f'git add {target}', check=True)


def commit_message(src:os.PathLike) -> str:
    commit = git.last_commit_message(src).replace(' [mv]', '')
    parent = git.last_commit_hash(src)
    return commit+'\n\nprevious commit: '+parent


for pid in range(1000, 30001):
    prob_src = os.path.join(str(pid//1000*1000), str(pid))
    prob_dst = os.path.join('problem', str(pid))

    if os.path.exists(prob_src):
        print(f'문제번호: {pid}')

        os.makedirs(prob_dst, exist_ok=True)

        for src in glob.glob(os.path.join(prob_src, '*.py')):
            dst = src.replace(prob_src, prob_dst)

            commit = commit_message(src)
            git.move(src, dst)
            git.commit(commit)

for gitkeep in glob.glob('**/.gitkeep', recursive=True):
    os.remove(gitkeep)
git.add('.')
git.commit('remove .gitkeep')
