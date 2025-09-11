def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health

    # 시뮬레이션은 마지막 공격 시점까지만 하면 충분
    last_time = attacks[-1][0] if attacks else 0
    atkidx = 0
    healtime = 0

    # 1초부터 last_time까지 진행
    for sec in range(1, last_time + 1):
        # 만약 이번 초가 공격 초라면
        if atkidx < len(attacks) and attacks[atkidx][0] == sec:
            damage = attacks[atkidx][1]
            health -= damage
            healtime = 0            # 연속 회복 끊김
            atkidx += 1
            if health <= 0:
                return -1
        else:
            # 공격이 없는 초에만 회복
            health += x
            healtime += 1
            if healtime == t:
                health += y
                healtime = 0        # 사이클 리셋
            if health > max_health:
                health = max_health

    return health