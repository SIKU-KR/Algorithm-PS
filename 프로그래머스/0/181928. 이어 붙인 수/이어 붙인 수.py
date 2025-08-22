def solution(num_list):
    odds = ''
    evens = ''
    for i in num_list:
        if i % 2 == 1:
            odds += str(i)
        else:
            evens += str(i)
    answer = int(odds) + int(evens)
    return answer