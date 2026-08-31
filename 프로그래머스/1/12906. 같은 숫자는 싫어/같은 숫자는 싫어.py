def solution(arr):
    stk = []
    for i in arr:
        if stk and stk[-1] == i:
            continue
        stk.append(i)
        
    return stk