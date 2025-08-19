# A형-1. 나무의 키

# import sys
# sys.stdin = open("Sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    # 가장 키가 큰 나무 (기준)
    max_h = max(trees)
    # 키 차이
    diff_h = [max_h - tree for tree in trees]

    # 키 차이가 모두 0이라면 바로 출력
    if sum(diff_h) == 0:
        print(f'#{tc} 0')
        continue

    # 필요한 +1 성장(홀수 날)과 +2 성장(짝수 날)의 총량을 계산한다.
    ones_needed = 0  # 반드시 +1로 채워야 하는 횟수
    twos_needed = 0  # +2로 채워야 하는 총량
    for d in diff_h:
        if d % 2 == 1:
            ones_needed += 1
        twos_needed += d // 2

    # 날짜별로 물주기
    day = 0
    ones_count = 0  # 현재까지 누적된 홀수 날
    twos_count = 0  # 현재까지 누적된 짝수 날

    # 키 차이가 모두 0이 되면 물주기를 종료한다.
    while True:
        # +1 필요량이 아직 다 채워지지 않았다면, 홀수 날을 우선적으로 채운다.
        if ones_count < ones_needed:
            # 홀수 날이 더 필요하다면, 날짜를 2씩 늘려 홀수 날을 확보한다.
            # 이때 짝수 날도 함께 증가한다.
            if day % 2 == 1:
                day += 2
            else:
                day += 1

        # +1 필요량이 충족되면, +2 필요량을 채운다.
        else:
            # 남은 홀수 날(2일 = 성장치 2)과 짝수 날로 +2 총량을 채울 수 있는지 확인한다.
            if twos_count + (ones_count - ones_needed) // 2 >= twos_needed:
                break  # 채울 수 있다면 종료, 현재 day가 정답
            else:
                day += 1  # 못 채우면 하루 더 진행한다.
        
        # 날짜가 증가함에 따라 사용 가능한 날짜 수 업데이트
        ones_count = (day + 1) // 2
        twos_count = day // 2

    print(f'#{tc} {day}')