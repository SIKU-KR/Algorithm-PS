def solution(code):
    answer = ''
    mode = False
    idx = 0
    for c in code:
        if mode:
            if c == '1':
                mode = False
            else:
                if idx % 2 == 1:
                    answer += c
        else:
            if c == '1':
                mode = True
            else:
                if idx % 2 == 0:
                    answer += c
        idx += 1
    if answer == '':
        return "EMPTY"
    else:
        return answer