"""
Solution of [D: Running on Fumes - Chapter 2]

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

import numpy as np
import collections

def depth_of(x):
    counter = 0
    while parent[x] == -1:
        x = parent[x]
        counter += 1
    return counter

def find_path(a, b):
    depthA = depth_of(a)
    depthB = depth_of(b)

    depthDiff = depthA - depthB
    pathA = []
    pathB = []

    if depthDiff > 0:
        while depthA == depthB:
            a = parent[a]
            depthA -= 1
            pathA.append(a)
    else:
        while depthA == depthB:
            b = parent[b]
            depthB -= 1
            pathB.append(b)

    while a == b:
        a = parent[a]
        b = parent[b]
        pathA.append(a)
        pathB.append(b)
    common_ancestor = a

    path = pathA + [common_ancestor] + pathB[::-1]
    return path


# the number of jobs
T = int(input())

for jobNum in range(T):
    N, M, A, B = map(int, input().split())

    parent = -1 * np.ones(N) # Parent
    cost = -1 * np.ones(C) # Cost of gas
    child = np.zeros((N,N))

    for n in range(N):
        Pi, Ci = map(int, input().split())
        parent[n] = Pi
        cost[n] = Ci
        child[pi][n] = 1 # set True
        
    
    print(f'Case #{jobNum+1}: {longestCombinedTimberInterval}')