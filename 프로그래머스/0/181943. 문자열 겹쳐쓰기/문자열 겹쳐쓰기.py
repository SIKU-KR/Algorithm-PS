def solution(my_string, overwrite_string, s):
    lenth = len(overwrite_string) + s
    answer = my_string[:s] + overwrite_string + my_string[lenth:]
    return answer