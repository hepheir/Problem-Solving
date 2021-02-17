import os
import glob

for file in glob.glob('**/*.py*', recursive=True):
    filename, ext = os.path.splitext(file)
    if ext != '.py':
        newfile = file.replace('.py', '').replace('  ', ' ') + '.py'
        os.rename(file, newfile)