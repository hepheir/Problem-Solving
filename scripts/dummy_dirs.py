import os

for i in range(1000, 20000+1, 1000):
    dirname = str(i)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(os.path.join(dirname, '.gitkeep'), 'w'):
        pass