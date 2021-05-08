import collections


def solution(v):
    '''
    3개의 좌표에서 x와 y값이 각각 1번씩 밖에 등장하지 않았으면,
    해당 x, y의 조합을 반환.
    '''
    answer = []

    x_cnt = collections.defaultdict(lambda: 0)
    y_cnt = collections.defaultdict(lambda: 0)

    for x, y in v:
        x_cnt[x] += 1
        y_cnt[y] += 1

    for x, cnt in x_cnt.items():
        if cnt == 1:
            answer.append(x)
            break

    for y, cnt in y_cnt.items():
        if cnt == 1:
            answer.append(y)
            break

    return answer