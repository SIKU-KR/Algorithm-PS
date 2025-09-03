def get_ivldidx(startday):
    if startday == 1:
        return [6, 7]
    elif startday == 2:
        return [5, 6]
    elif startday == 3:
        return [4, 5]
    elif startday == 4:
        return [3, 4]
    elif startday == 5:
        return [2, 3]
    elif startday == 6:
        return [1, 2]
    elif startday == 7:
        return [7, 1]

def isOk(plan, real):
    h, m = divmod(plan, 100)
    m += 10
    if m >= 60:
        h += 1
        m -= 60
    plan_after = h * 100 + m
    return real <= plan_after
    
def solution(schedules, timelogs, startday):
    answer = 0
    
    invalid_index = get_ivldidx(startday)
    for i in range(len(schedules)):
        plan = schedules[i]
        person = timelogs[i]
        success = True
        
        for t in range(len(person)):
            if t + 1 not in invalid_index and not isOk(plan, timelogs[i][t]):
                success = False
                break
                
        if success:
            answer += 1
    return answer
