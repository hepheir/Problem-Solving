import sys

data_num = 0
sys.stdin = open(f'contest\\616 EtvycAuRLZpb6hhe86x0\\4 ꓮ번 - 두 천재들의 대결\\data\\boj\\sample\\{data_num}.in', 'r')



board = dict()

board['A1'] = '+R'
board['B1'] = '+K'
board['C1'] = '+B'
board['B2'] = '+P'

board['C4'] = '+R'
board['B4'] = '+K'
board['A4'] = '+B'
board['B3'] = '+P'



for n in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()
    player = line[0]
    pick = line[1:3]
    put = line[3:5]
    type = line[5]

