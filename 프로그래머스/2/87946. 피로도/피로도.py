from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        current = k
        cnt = 0
        for essential, reduce in i:
            if current >= essential:
                current -= reduce
                cnt += 1
        answer = max(answer, cnt)
    return answer
                