def solution(s):
    li = s.split(" ")
    for i in range(len(li)):
        if li[i]:
            li[i] = li[i][0].upper() + li[i][1:].lower()
    return " ".join(li)