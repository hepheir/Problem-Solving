"""
Written by hepheir@gmail.com
2020-07-26
"""

import sys


filePaths = {
    'sample' : '2020/Qualification Round/Problems/A - Travel Restrictions/sample_input.txt',
    'validation' : '2020/Qualification Round/Problems/A - Travel Restrictions/travel_restrictions_validation_input.txt',
    'grade' : '2020/Qualification Round/Problems/A - Travel Restrictions/travel_restrictions_input.txt'
}

inputFilePath = filePaths['grade']
outputFilePath = inputFilePath.replace('input', 'output')

sys.stdin = open(inputFilePath, 'r')
sys.stdout = open(outputFilePath, 'w')


def is_flight_available(I, O, i, j):
    """
    I: incoming flights restriction
    O: outgoing flights restriction
    i: source country
    j: destination country
    """
    distance = j-i
    if distance == 0:
        return 'Y'
    direction = distance // abs(distance)
    for current_i in range(i, j, direction):
        current_j = current_i + direction
        if O[current_i] == 'N' or I[current_j] == 'N':
            return 'N'
    return 'Y'

airlines = T = int(input())
for a in range(airlines):
    print(f'Case #{a+1}:')

    N = int(input())
    I = input()
    O = input()
    
    for i in range(N):
        P = ''
        for j in range(N):
            P += is_flight_available(I, O, i, j)
        print(P)