def solution(progresses, speeds):
    answer = []
    while progresses and speeds:
        count = 0
        while progresses[0] < 100:
            for i in range(0, len(progresses)):
                progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        answer.append(count)
    return answer