#!usr/env/python

"""
Written by hepheir@gmail.com
Problem solution for CPS Festival

used Python 3.8.0 64-bit
"""

from __future__ import annotations

def g(a:int, b:int) -> set:
    """
    기어값(g)은 체인링 숫자 세트와 콕셋 수자 세트에서 하나씩 선택한 두 숫자 a, b의 곱 (axb)과
    두 숫자의 곱보다 1 크거나 작은 값의 조합((axb)-1, axb, (axb)+1)을 의미합니다.
    
    TC: O(1)
    """
    x = a*b
    return set((x-1, x, x+1))

def max_g(s1:set, s2:set)->int:
    """
    두 숫자 세트를 이용하여 1부터 n사이의 모든 기어값을 만들 수 있을 때, n의 최댓값.
    
    TC: O(len(s1) * len(s2))
    """
    s = set()
    for i1 in s1:
        for i2 in s2:
            s = s | g(i1, i2)
    s.add(0)
    for idx, val in enumerate(sorted(s)):
        if val != idx:
            return idx
    return len(s) - 1


def set_generator(setSize:int, maxGearValue:int) -> set:
    """
    숫자 세트 크기가 `setSize`이고 최대 기어값이 `maxGearValue`인 기어 설계에 필요한 숫자 세트를 찾는다.
    숫자 set을 반환하는 Generator 객체를 반환한다.
    
    TC: O( (len(s1) * len(s2))^2 )
    """
    answer = set(range(maxGearValue, 0, -1))
    for s1 in comb(answer, setSize):
        for s2 in comb(answer, setSize):
            mg = max_g(s1, s2)
            if mg >= maxGearValue:
                yield s1, s2

    # for intSet in comb(range(maxGearValue), )

def comb(intSet:set, setSize:int) -> set:
    """
    `intSet` 주어진 정수 집합에서 `setSize`개 만큼만 선택하여 만들 수 있는 세트의 모든 경우의 수를 순차적으로 반환한다.
    숫자 set을 반환하는 Generator 객체를 반환한다.

    TC: O(N^2)
    """
    statusRegister = 0
    inList = list(intSet)
    inSetSize = len(inList)
    exSetSize = setSize
    while not ((statusRegister >> inSetSize) & 1):
        binString = f'{statusRegister:0{inSetSize}b}'
        if sum(map(int, binString)) == exSetSize:
            exSet = set()
            for shr in range(inSetSize):
                if binString[shr] == '1':
                    exSet.add(inList[inSetSize-1-shr])
            yield exSet
        statusRegister += 1

print(list(set_generator(6, 56)))
