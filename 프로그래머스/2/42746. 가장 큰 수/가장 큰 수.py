def solution(numbers):
    numbers_str = []
    for i in range(len(numbers)):
        numbers_str.append((i, str(numbers[i]) * 4, numbers[i]))
    numbers_str.sort(key=lambda x: x[1], reverse=True)
    answer = ""
    for _, _, a in numbers_str:
        answer += str(a)
    if answer[0] == "0":
        return '0'
    return answer