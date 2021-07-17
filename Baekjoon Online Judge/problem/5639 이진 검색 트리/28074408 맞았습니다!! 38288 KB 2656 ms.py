# 참고 영상
# Preorder to Postorder in BST
# https://www.youtube.com/watch?v=0QOtVxTVj4w

import sys

sys.setrecursionlimit(10**5)


def subtree(array, start, end):
    if (start >= len(array)) or (start > end):
        return

    root = array[start]

    if (end > start):
        for mid in range(start, end+1):
            if array[mid] > root: break
        else: mid += 1
        mid -= 1

        subtree(array, start+1, mid)
        subtree(array, mid+1, end)

    print(root)


def solve():
    preorder = list(map(int, sys.stdin.readlines()))
    subtree(preorder, 0, len(preorder)-1)

solve()