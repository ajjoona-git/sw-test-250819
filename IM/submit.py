# import sys
# sys.stdin = open("Sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 1번 방 ~ N번 방의 왼쪽 방향으로 연결된 포탈의 방 번호
    # 인덱스 0은 사용하지 않는다.
    portal = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)

    # 1번 방부터 시작한다
    i = 1
    count = 0
    visited[1] = True

    # 제일 오른쪽 방(N)에 도착하면 게임이 끝난다.
    while 1 <= i < N:
        count += 1
        # 방문했던 방이면, 오른쪽 방으로 이동한다.
        if visited[i]:
            i += 1
        # 처음 방문하는 방이면, 왼쪽 포탈(p[i])로 이동한다.
        else:
            visited[i] = True
            i = portal[i]

        # print(f'{count}번째 포탈 이동: {i}')

    print(f'#{tc} {count}')