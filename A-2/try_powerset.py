# A형-2. 면접

# import sys
# sys.stdin = open('Sample_input.txt')


def make_subset(N, M):
    """N개 집합에서 M개 원소인 부분집합 구하기"""
    # indicies = list(range(N))
    subsets = []

    for i in range(1<<N):
        current_subset = []
        for j in range(N):
            if (1<<j) & i:
                current_subset.append(j)
                if len(current_subset) > M:
                    break
        if len(current_subset) == M:
            subsets.append(current_subset)

    return subsets


T = int(input())
for tc in range(1, T+1):
    # N개 문제 중 M개를 맞춤. K는 카운터
    N, M, K = map(int, input().split())

    # 최소 점수
    min_score = float('inf')

    subsets = make_subset(N, M)

    for answer_idx in subsets:
        counter = 0
        score = 0

        for i in range(N):
            # 문제를 맞추는 경우
            if i in answer_idx:
                counter += 1
                score += 1
                if counter == K:
                    counter = 0
                    score *= 2
                if score > min_score:
                    break
            # 문제를 틀리는 경우
            else:
                counter = 0

        if score < min_score:
            min_score = score

    print(f'#{tc} {min_score}')