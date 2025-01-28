def solution(nums):
    half = len(nums) // 2
    dic = set()
    for i in nums:
        dic.add(i)
    if len(dic) > half:
        return half
    else:
        return len(dic)