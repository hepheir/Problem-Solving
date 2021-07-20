"""
Solution of [C: Timber]

Written by hepheir@gmail.com
2020-07-26 / Python 3.8.0
"""

from __future__ import annotations

# ================================================================
# Override stdin / stdout for validations.

import sys

filePaths = {
    'sample' : '2020/Qualification Round/Problems/C - Timber/data/sample_input.txt',
    'valid' : '2020/Qualification Round/Problems/C - Timber/data/timber_validation_input.txt',
    'submission' : '2020/Qualification Round/Problems/C - Timber/data/timber_input.txt'
}

inputFilePath = filePaths['submission']
outputFilePath = inputFilePath.replace('input', 'output')

sys.stdin = open(inputFilePath, 'r')
sys.stdout = open(outputFilePath, 'w')

# ================================================================
# Solution

class Tree:
    def __init__(self, position:int, height:int) -> Tree:
        self.position:int = position
        self.height:int = height
        self.left:list = []
        self.right:list = []

# the number of forest sections
T = int(input())

for sectionNum in range(T):
    N = int(input()) # the number of trees
    trees = []
    for treeNum in range(N):
        # Pi: position of the tree
        # Hi: height of the tree (in metres)
        Pi, Hi = map(int, input().split(' '))
        trees.append(Tree(Pi-Hi, 0)) # Add dummy tree to make calculation easy.
        trees.append(Tree(Pi, Hi))
        trees.append(Tree(Pi+Hi, 0)) # Add dummy tree to make calculation easy.

    # Connects Trees - O(N^2)
    for treeNum, tree in enumerate(trees):
        for leftTreeNum, leftTree in enumerate(trees):
            if tree.position == (leftTree.position + leftTree.height):
                tree.left.append(leftTreeNum) # direction of the connection: treeNum <- leftTreeNum
        for rightTreeNum, rightTree in enumerate(trees):
            if tree.position == (rightTree.position - rightTree.height):
                tree.right.append(rightTreeNum) # direction of the connection: treeNum <- rightTreeNum

    longestCombinedTimberInterval = 0

    for rootTreeNum in range(len(trees)):
        # Find left most tree (using dfs)
        visited = []
        stack = [rootTreeNum]
        leftEnd = trees[rootTreeNum].position
        while stack:
            tn = stack.pop()
            if tn not in visited:
                visited.append(tn)
                leftEnd = min(leftEnd, trees[tn].position)
                stack += list(set(trees[tn].left) - set(visited))

        # Find right most tree (using dfs)
        visited = []
        stack = [rootTreeNum]
        rightEnd = trees[rootTreeNum].position
        while stack:
            tn = stack.pop()
            if tn not in visited:
                visited.append(tn)
                rightEnd = max(rightEnd, trees[tn].position)
                stack += list(set(trees[tn].right) - set(visited))
        
        combinedTimberInterval = rightEnd - leftEnd
        longestCombinedTimberInterval = max(combinedTimberInterval, longestCombinedTimberInterval)
    
    print(f'Case #{sectionNum+1}: {longestCombinedTimberInterval}')