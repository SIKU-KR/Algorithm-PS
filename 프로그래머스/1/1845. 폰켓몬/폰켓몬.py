from collections import Counter

def solution(nums):
    n = len(nums)
    cnt = n // 2
    dic = Counter(nums)
    # print(dic.most_common(cnt))
    return len(dic.most_common(cnt))