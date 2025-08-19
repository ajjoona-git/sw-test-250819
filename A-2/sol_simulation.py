# A형-2. 면접
# 시뮬레이션을 통한 직관적인 풀이
# '최소 점수 전략은 보너스를 가능한 한 빨리, 몰아서 받는 것이다'

import sys
sys.stdin = open('Sample_input.txt')


def count_score(N, M, K):
    # 1. 보너스를 피할 수 있는지 확인한다.

    # num_incorrect: 틀린 문항 수(칸막이 역할)
    num_incorrect = N - M
    # num_slots: 틀린 문제들로 만들 수 있는 공간의 수
    num_slots = num_incorrect + 1
    # safe_capacity: 보너스를 피할 수 있는 문항 수
    # 각 공간에 K-1개씩 문제를 넣으면 보너스를 피할 수 있다.
    safe_capacity = num_slots * (K - 1)

    # 만약 맞춰야 할 문제 수가 safe_capacity 이하라면, 보너스 없이 1점씩만 받는다.
    if M <= safe_capacity:
        return M

    # 2. 보너스를 피할 수 없는 경우라면, 점수 시뮬레이션

    # must_bonus_problems: safe_capacity 초과분
    # 보너스를 반드시 받아야 하는 문항의 수
    must_bonus_problems = M - safe_capacity
    # num_bonus_groups: must_bonus_problems로 만들어야 하는 최소 보너스 묶음의 수
    num_bonus_groups = (must_bonus_problems + K - 1) // K

    # [최소 점수 전략] 보너스 묶음을 초반에 모두 푼다고 가정한다.
    # bonus_score: 보너스 묶음 D개를 모두 풀었을 때의 점수
    # (k*2^D + k*2^(D-1) + ... + k*2^1) = 2k * (2^D - 1)
    bonus_score = 2 * K * (2 ** num_bonus_groups - 1)
    # 보너스 묶음을 만들고도 남은 문제들은 보너스 없이 1점씩만 획득한다.
    remaining_score = M - num_bonus_groups * K

    return bonus_score + remaining_score



T = int(input())
for tc in range(1, T+1):
    # N개 문제 중 M개를 맞춤. K는 카운터
    N, M, K = map(int, input().split())
    print(f'#{tc} {count_score(N, M, K)}')