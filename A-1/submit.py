# A형-1. 나무의 키

# import sys
# sys.stdin = open("Sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    # 가장 키가 큰 나무 (기준)
    max_h = 0
    for tree in trees:
        if tree > max_h:
            max_h = tree

    # 키 차이
    diff_h = [0] * N
    for i, tree in enumerate(trees):
        diff_h[i] = max_h - tree

    # 날짜별로 물주기
    day = 0

    # 키 차이가 모두 0이 되면 물주기를 종료한다.
    while max(diff_h) != 0:
        day += 1

        # 홀수 번째 날은 diff_h가 홀수인 나무에,
        if day % 2 == 1:
            for i in range(N):
                if diff_h[i] > 0 and diff_h[i] % 2 == 1:
                    diff_h[i] -= 1
                    break
            # 만약 키차이가 홀수인 나무는 없지만, 2이상인 나무가 있다면 물주기
            else:
                for i in range(N):
                    if diff_h[i] > 2:
                        diff_h[i] -= 1
                        break

        # 짝수 번째 날은 diff_h가 짝수인 나무에
        else:
            for i in range(N):
                if diff_h[i] > 0 and diff_h[i] % 2 == 0:
                    diff_h[i] -= 2
                    break

    print(f'#{tc} {day}')