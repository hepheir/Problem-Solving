import collections


def solution(n, start, end, roads, traps):
    answer = 0
    node = start
    deque = collections.deque([(start)])

    return answer