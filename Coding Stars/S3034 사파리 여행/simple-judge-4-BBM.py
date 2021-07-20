# ================================
#  Solution
# ================================

import sys
import io


def solve():
    total, diff = map(int, input().split()) # 351 8
    large = (total/2)+(diff/2) # 175.5 + 4 = 179.5
    small = (total/2)-(diff/2) # 175.5 - 4 = 171.5
    if small > 0:
        if diff/2 - int(diff/2) == 0:
            large = int(large)
            small = int(small)
            print(large, small)
        else:
            print('impossible')
    else:
        print('impossible')

# ================================
#  Judge
# ================================


default_stdout = sys.stdout

# 가상 입출력 스트림 생성
sys.stdout = io.TextIOWrapper(io.BytesIO())
sys.stdin = io.TextIOWrapper(io.BytesIO())

SAMPLE_INPUT = '''33
50 20
50 21
50 60
338 181
351 8
393 887
528 597
388 206
873 884
572 124
909 543
96 607
768 661
724 378
535 975
765 597
404 759
753 442
385 99
201 119
327 457
577 938
53 462
484 802
75 729
527 350
340 197
969 137
452 307
762 700
474 296
932 660
843 216
'''

# 첫 번째 줄: 총 테스트 케이스의 개수 T
# 1~(T+1) 번째 줄: 각 테스트 케이스의 입력
sys.stdin.write(SAMPLE_INPUT)
sys.stdin.seek(0)

ANSWER = '''35 15
impossible
impossible
impossible
impossible
impossible
impossible
297 91
impossible
348 224
726 183
impossible
impossible
551 173
impossible
681 84
impossible
impossible
242 143
160 41
impossible
impossible
impossible
impossible
impossible
impossible
impossible
553 416
impossible
731 31
385 89
796 136
impossible
'''

if __name__ == '__main__':
    TESTCASES = int(input())
    for t in range(TESTCASES):
        solve()

    sys.stdout.seek(0)
    SUBMITTED_ANSWER = sys.stdout.read()  # 가상 STDOUT 출력값 확인
    default_stdout.write(SUBMITTED_ANSWER)  # 콘솔에도 출력
    default_stdout.write('\n======== 결과 =========\n')
    default_stdout.write(f'정답: {ANSWER.rstrip() == SUBMITTED_ANSWER.rstrip()}\n\n')

    sample_lines = SAMPLE_INPUT.split("\n")
    default_stdout.write('\n======== 줄 번호 / 입력 / 원래 정답 / 오답 =========\n')
    for idx, ans_line, sub_line in zip(range(100), ANSWER.split('\n'), SUBMITTED_ANSWER.split('\n')):
        if ans_line != sub_line:
            default_stdout.write(f'{idx:2d} [{sample_lines[1+idx]}] [{ans_line}] [{sub_line}]\n')
