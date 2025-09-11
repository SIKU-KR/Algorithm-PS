def get_index(str):
    if str == "code":
        return 0
    elif str == "date":
        return 1
    elif str == "maximum":
        return 2
    else:
        return 3

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_idx = get_index(ext)
    sort_idx = get_index(sort_by)
    for i in data:
        if i[ext_idx] < val_ext:
            answer.append(i)
    answer.sort(key = lambda x:x[sort_idx])
    return answer