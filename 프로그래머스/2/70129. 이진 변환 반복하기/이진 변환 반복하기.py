def binary_conversion(x):
    cnt = x.count("0")
    c = len(x) - cnt
    return list(bin(c)[2:]), cnt
    
def solution(s):
    loop_cnt = 0
    remove_cnt = 0
    ar = list(s)
    while ar != ["1"]:
        ar, j = binary_conversion(ar)
        loop_cnt += 1
        remove_cnt += j
    return [ loop_cnt, remove_cnt ]