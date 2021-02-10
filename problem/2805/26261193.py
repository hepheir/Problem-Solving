import sys

N, M = map(int, sys.stdin.readline().split())
heights_of_trees = list(map(int, sys.stdin.readline().split()))
heights_of_trees.sort(reverse=True) # 내림차순 정렬

def cut_tree(cutter_h):
    # h의 높이에서 톱날로 잘랐을 때, 상근이가 들고 갈 나무의 미터 수
    retval = 0
    for tree_h in heights_of_trees:
        if tree_h <= cutter_h:
            # 내림차순으로 정렬되어있으므로
            # 뒤는 더 보지 않아도 됨
            break
        retval += max(0, tree_h-cutter_h)
    return retval


def bin_search(decending_ordered_array, minimum):
    upper = decending_ordered_array[0]
    lower = decending_ordered_array[-1]
    answer = 0
    while lower <= upper:
        mid = (upper+lower)//2
        cut = cut_tree(mid)
        if cut >= minimum:
            lower = mid+1
            answer = mid
        else:
            upper = mid-1
    return answer

print(bin_search(heights_of_trees, minimum=M))