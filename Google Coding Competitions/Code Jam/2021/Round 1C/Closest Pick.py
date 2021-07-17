import sys
import math
import heapq


def max_heap_push(heap, x):
    heapq.heappush(heap, -x)


def max_heap_pop(heap):
    return -heapq.heappop(heap)


def max_heap_top(heap):
    if heap:
        return -heap[0]
    else:
        return 0


def max_heap_2tops(heap):
    retval = 0
    if heap:
        retval += max_heap_pop(heap)
    if heap:
        retval += max_heap_pop(heap)
    return retval



def solve():
    N, K = map(int, sys.stdin.readline().split())
    P = set(map(int, sys.stdin.readline().split()))

    one_card_heap = []
    two_cards_heap = []

    last_p = 0
    for p in sorted(P):
        if not last_p:
            dist = p-1
            max_heap_push(one_card_heap, dist)
            max_heap_push(two_cards_heap, dist)
        else:
            dist = p-last_p-1
            max_heap_push(one_card_heap, math.ceil((dist)/2))
            max_heap_push(two_cards_heap, dist)
        last_p = p
    max_heap_push(one_card_heap, K-last_p)
    max_heap_push(two_cards_heap, K-last_p)

    one_card_ans = max_heap_2tops(one_card_heap)
    two_cards_ans = max_heap_top(two_cards_heap)

    return max(one_card_ans, two_cards_ans) / K


T = int(sys.stdin.readline())
for x in range(1, T+1):
    print("Case #{x}: {y}".format(x=x, y=solve()))