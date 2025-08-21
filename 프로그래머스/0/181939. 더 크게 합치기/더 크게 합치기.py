def solution(a, b):
    answer_a = int(str(a) + str(b))
    answer_b = int(str(b) + str(a))
    if answer_a > answer_b:
        return answer_a
    else:
        return answer_b