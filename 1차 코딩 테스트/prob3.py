from collections import defaultdict, deque


def zip_arr(tup: tuple) -> tuple:
    """ 이미 정렬된 원소를 제외한 나머지 원소만
    """
    ret_arr = []
    for i, val in enumerate(tup):
        if val != i:
            ret_arr.append(val)
    for i in range(len(ret_arr)):
        while i not in ret_arr:
            for j in range(len(ret_arr)):
                if ret_arr[j] > i:
                    ret_arr[j] -= 1
    return tuple(ret_arr)


def swap_arr(tup: tuple, i: int, j: int) -> tuple:
    ret_arr = list(tup)
    ret_arr[i], ret_arr[j] = ret_arr[j], ret_arr[i]
    return tuple(ret_arr)


def solution(arr, k):
    arr = zip_arr(arr)
    if not arr:
        return 0
    queue = deque([arr])
    visited = defaultdict(lambda: False)
    depth = 1
    while queue:
        width = len(queue)
        for w in range(width):
            cur_arr = queue.popleft()
            cur_size = len(cur_arr)
            if visited[cur_arr]:
                continue
            else:
                visited[cur_arr] = True
                for i in range(cur_size):
                    for j in range(i+1, min(i+k+1, cur_size)):
                        swapped_arr = swap_arr(cur_arr, i, j)
                        zipeed_arr = zip_arr(swapped_arr)
                        if not zipeed_arr:
                            return depth
                        else:
                            queue.append(zipeed_arr)
        depth += 1
    return depth


print(solution([4, 5, 2, 3, 1], 2))
print(solution([5, 4, 3, 2, 1], 4))
