import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking = {}      # 입차 시간 기록: {차량번호: 입차시간(분)}
    total_time = {}   # 누적 주차 시간: {차량번호: 총시간(분)}
    
    # 1. 기록 순회하며 누적 주차 시간 계산
    for r in records:
        time_str, car, action = r.split()
        h, m = map(int, time_str.split(':'))
        t = h * 60 + m
        
        if action == 'IN':
            parking[car] = t
        else:
            duration = t - parking.pop(car)
            total_time[car] = total_time.get(car, 0) + duration

    # 2. 23:59까지 출차하지 않은 차량 정산
    end_of_day = 23 * 60 + 59
    for car, in_time in parking.items():
        duration = end_of_day - in_time
        total_time[car] = total_time.get(car, 0) + duration

    # 3. 차량 번호 오름차순으로 최종 요금 계산 및 반환
    result = []
    for car in sorted(total_time.keys()):
        time = total_time[car]
        if time <= base_time:
            result.append(base_fee)
        else:
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
            result.append(fee)
            
    return result