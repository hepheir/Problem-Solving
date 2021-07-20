"""
Solution of [B: Alchemy]

Written by hepheir@gmail.com
2020-07-26 / Python 3.8.0
"""

# ================================================================
# Override stdin / stdout for validations.

import sys

filePaths = {
    'sample' : '2020/Qualification Round/Problems/B - Alchemy/data/sample_input.txt',
    'valid' : '2020/Qualification Round/Problems/B - Alchemy/data/alchemy_validation_input.txt',
    'grade' : '2020/Qualification Round/Problems/B - Alchemy/data/alchemy_input.txt'
}

inputFilePath = filePaths['grade']
outputFilePath = inputFilePath.replace('input', 'output')

sys.stdin = open(inputFilePath, 'r')
sys.stdout = open(outputFilePath, 'w')

# ================================================================
# Solution

# brute force
cheatSheet = {
    'AAB': 'A',
    'ABA': 'A',
    'ABB': 'B',
    'BAA': 'A',
    'BAB': 'B',
    'BBA': 'B',
}


T = int(input()) # the number of Philosopher's Stones

for stoneNum in range(T):
    N = int(input())
    C = input()

    answer = 'Y'
    while len(C) > 1:
        length = len(C)
        for key in cheatSheet:
            C = C.replace(key, cheatSheet[key])
        if length == len(C):
            # no replacable -> dead end
            answer = 'N'
            break
    
    print(f'Case #{stoneNum+1}: {answer}')