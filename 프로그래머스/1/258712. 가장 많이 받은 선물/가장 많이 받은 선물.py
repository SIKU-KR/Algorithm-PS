def solution(friends, gifts):
    # 친구 인덱스 매핑
    idx = {name: i for i, name in enumerate(friends)}
    n = len(friends)

    # 선물 카운트 행렬과 선물지수
    fgl = [[0]*n for _ in range(n)]
    points = [0]*n

    # 기록 반영
    for s in gifts:
        a, b = s.split()
        ia, ib = idx[a], idx[b]
        fgl[ia][ib] += 1
        points[ia] += 1
        points[ib] -= 1

    # 다음 달 "받을" 선물 개수
    receive = [0]*n

    # 모든 무방향 쌍을 정확히 한 번만 비교
    for i in range(n):
        for j in range(i+1, n):
            a_to_b = fgl[i][j]
            b_to_a = fgl[j][i]

            if a_to_b > b_to_a:
                receive[i] += 1
            elif b_to_a > a_to_b:
                receive[j] += 1
            else:
                if points[i] > points[j]:
                    receive[i] += 1
                elif points[j] > points[i]:
                    receive[j] += 1
                # 같으면 변화 없음

    return max(receive)