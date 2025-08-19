# A형-2. 면접

import sys
sys.stdin = open('Sample_input.txt')



T = int(input())
for tc in range(1, T+1):
    # N개 문제 중 M개를 맞춤. K는 카운터
    N, M, K = map(int, input().split())

    # 최소 점수
    min_score = float('inf')


    counter = 0
    score = 0
    answer = 0

    for i in range(1>>N):
        for j in range(N):
            if (1<<j) & i:
            # 문제를 맞추는 경우
                counter += 1
                score += 1
                answer += 1
                if counter == K:
                    counter = 0
                    score *= 2
                if score > min_score:
                    break
                if answer > M:
                    break
            # 문제를 틀리는 경우
            else:
                counter = 0

        if answer == M and score < min_score:
            min_score = score

    print(f'#{tc} {min_score}')