"""
Solution of [D: Running on Fumes - Chapter 1]

Written by hepheir@gmail.com
2020-07-27 / Python 3.8.0
"""

# ================================================================
# Override stdin / stdout for validations.

import sys

filePaths = {
    'sample' : '2020/Qualification Round/D1 - Running on Fumes - Chapter 1/data/sample_input.txt',
    'valid' : '',
    'submission' : ''
}

inputFilePath = filePaths['sample']
outputFilePath = inputFilePath.replace('input', 'output')

sys.stdin = open(inputFilePath, 'r')
sys.stdout = open(outputFilePath, 'w')

# ================================================================
# Solution

nextCity = []
gasCost = []

# the number of jobs
T = int(input())

for jobNum in range(T):
    N, M = map(int, input().split())

    for n in range(N):
        Ci = int(input())
        nextCity.append(n+1)
        gasCost.append(Ci)
    
    print(f'Case #{jobNum+1}: {longestCombinedTimberInterval}')