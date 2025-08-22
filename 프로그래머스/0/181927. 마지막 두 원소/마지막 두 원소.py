def solution(num_list):
    length = len(num_list)
    last = num_list[length-1]
    lasttwo = num_list[length-2]
    if last > lasttwo:
        num_list.append(last-lasttwo)
    else:
        num_list.append(last*2)
    return num_list