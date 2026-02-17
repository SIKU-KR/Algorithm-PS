def solution(arr):
    if len(arr) == 1:
        return [-1]
    x = min(arr)
    arr.remove(x)
    return arr