# A형-2. 면접

# import sys
# sys.stdin = open('Sample_input.txt')


def calculate_score(i, score=0, answer=0, counter=0):
    # score = 0  # 점수
    # answer = 0  # 정답인 문제 수
    # counter = 0  # 연속 정답의 수
    global min_score

    # counter가 K인 경우, 점수 두 배
    if counter == K:
        counter = 0
        score *= 2

    # 현재 점수가 최저 점수보다 큰 경우 더이상 점수계산 하지 않음
    if score > min_score:
        return None

    # M개 정답인 경우, 최저 점수를 갱신함
    elif answer == M:
        if score < min_score:
            min_score = score
        return None

    # N개 문제를 모두 탐색한 경우 종료
    elif i > N:
        return None

    # 남은 문제보다 맞춰야할 정답 수가 많다면 종료
    elif (N - i) < (M - answer - 1):
        return None


    # i번 문제가 정답인 경우
    calculate_score(i + 1, score + 1, answer + 1, counter + 1)

    # i번 문제가 오답인 경우
    calculate_score(i + 1, score, answer, 0)



T = int(input())
for tc in range(1, T+1):
    # N개 문제 중 M개를 맞춤. K는 카운터
    N, M, K = map(int, input().split())

    # 최소 점수
    min_score = float('inf')

    calculate_score(1, 0, 0, 0)

    print(f'#{tc} {min_score}')