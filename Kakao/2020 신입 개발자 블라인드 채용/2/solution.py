from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    comb_count = defaultdict(lambda: 0)
    # Step1: 각 메뉴 조합별 주문 횟수 세기
    for order in orders: # n
        for n_menus in course: # k
            for comb in combinations(order, n_menus): # nCk
                comb_count[comb] += 1
    # Step2: 코스 별, 후보 메뉴 찾기
    for menu in orders_count:
        for n_menus in course:
            if orders_count[menu] >= n_menus:
                candidate_menus[n_menus].append(menu)
    # Step3: 정답 작성
    for n_menus in candidate_menus:
        answer += map(lambda x: ''.join(x), combinations(candidate_menus[n_menus], n_menus))
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))