import glob
import os

for file in glob.glob(os.path.join(os.path.dirname(__file__), '**','*'), recursive=True):
    if ('.in' in file) or ('.out' in file):
        file, newfile = file, file.replace('boj.sample.', ''); os.rename(file, newfile)
        file, newfile = newfile, newfile.replace('boj.sample.', ''); os.rename(file, newfile)
