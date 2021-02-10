import collections
import sys


N, M = map(int, sys.stdin.readline().split())
heights_of_trees = collections.Counter(map(int, sys.stdin.readline().split()))

def cut_tree(cutter_h):
    # h의 높이에서 톱날로 잘랐을 때, 상근이가 들고 갈 나무의 미터 수
    retval = 0
    for tree_h, count in heights_of_trees.items():
        retval += max(0, tree_h-cutter_h) * count
    return retval


def bin_search(minimum):
    upper = 2000000000
    lower = 1
    answer = 0
    while lower <= upper:
        pivot = (upper+lower)//2
        cut = cut_tree(pivot)
        if cut >= minimum:
            lower = pivot+1
            answer = pivot
        else:
            upper = pivot-1
    return answer

print(bin_search(minimum=M))